# #!/bin/bash

# Update the ubonto server.
sudo apt update 

# Install java.
sudo apt install openjdk-11-jdk -y

#  Debian package repository of Jenkins to automate installation and upgrade.
curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee \
    /usr/share/keyrings/jenkins-keyring.asc > /dev/null
# Then add a Jenkins apt repository entry:
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
    https://pkg.jenkins.io/debian binary/ | sudo tee \
    /etc/apt/sources.list.d/jenkins.list > /dev/null

# Update your local package index, then finally install Jenkins:
sudo apt-get update
sudo apt-get install fontconfig openjdk-11-jre -y
sudo apt-get install jenkins -y

# Run jenkins
sudo systemctl start jenkins
sudo systemctl enable jenkins
