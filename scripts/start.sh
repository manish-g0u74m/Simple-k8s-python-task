#!/bin/bash
cd /home/ec2-user/app
docker stop myapp || true
docker rm myapp || true
docker pull $(cat imageDetail.json | jq -r '.ImageURI')
docker run -d --name myapp -p 80:80 $(cat imageDetail.json | jq -r '.ImageURI')
