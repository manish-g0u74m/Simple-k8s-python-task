from flask import Flask
AWS_ACCESS_KEY_ID="AKIA1234567890ABCDE"
AWS_SECRET_ACCESS_KEY="abcd1234abcd1234abcd1234abcd1234abcd1234"
app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>Welcome to the Kainskep Solutions!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
