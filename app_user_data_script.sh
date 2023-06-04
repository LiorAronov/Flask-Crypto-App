#!/bin/bash

# Update the Lincux server.
sudo yum update -y

# Install Python3 and pip3.
sudo yum install -y python3
sudo yum install -y python3-pip
# sudo apt install python3-pip

# Install git packages.
sudo yum install -y git

# Install requests library 
sudo pip3 install requests

git clone https://github.com/LiorAronov/Flask-Crypto-App.git
cd Flask-Crypto-App/Production-Env/app
# Installation of additional required packages.
sudo pip3 install -r requirements.txt


 pip3 install gunicorn

 gunicorn -b 0.0.0.0:8000 app:app
# Install AWS CLI for access to AWS services
# sudo yum install -y mawscli

# # Install Docker on the EC2 
# sudo amazon-linux-extras install docker
# sudo service docker start
# sudo usermod -a -G docker ec2-user


