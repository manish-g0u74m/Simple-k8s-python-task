import json
import os
import boto3
from botocore.exceptions import ClientError

SECRET_NAME = "DBPassword"   # secret Name in AWS Secrets Manager
REGION_NAME = "ap-south-1"
ENV_FILE_PATH = ".env"


def get_secret():
    
    # Fetch secret from AWS Secrets Manager
    
    session = boto3.session.Session()
    client = session.client(
        service_name="secretsmanager",
        region_name=REGION_NAME
    )

    try:
        response = client.get_secret_value(SecretId=SECRET_NAME)
    except ClientError as e:
        raise RuntimeError(f"Unable to fetch secret: {e}")

    secret_string = response.get("SecretString")
    
    if not secret_string:
        raise RuntimeError("SecretString is empty")

    return json.loads(secret_string)


def read_env_file():
    
   # Read existing .env file
    
    env_vars = {}

    if not os.path.exists(ENV_FILE_PATH):
        return env_vars

    with open(ENV_FILE_PATH, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, value = line.split("=", 1)
            env_vars[key] = value

    return env_vars


def write_env_file(env_vars):
    
    # Write dictionary values back to .env file
    
    with open(ENV_FILE_PATH, "w") as f:
        for key, value in env_vars.items():
            f.write(f"{key}={value}\n")


def update_env():
    print("Fetching secrets from AWS Secrets Manager...")
    secrets = get_secret()

    print("Reading existing .env file...")
    env_vars = read_env_file()

    print("Updating .env values...")
    for key, value in secrets.items():
        env_vars[key] = value

    write_env_file(env_vars)
    print(".env file updated successfully")


if __name__ == "__main__":
    update_env()
