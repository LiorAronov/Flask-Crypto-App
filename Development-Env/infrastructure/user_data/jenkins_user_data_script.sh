# #!/bin/bash

# Update the ubonto server.
sudo apt update -y


#  Debian package repository of Jenkins to automate installation and upgrade.
curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
# Then add a Jenkins apt repository entry:
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt update -y
# Install Java.
sudo apt-get install fontconfig openjdk-11-jre -y
# Install jenkins.
sudo apt-get install jenkins -y

# Run jenkins
sudo systemctl start jenkins
sudo systemctl enable jenkins

# Install Extensions.
sudo apt install git -y


# sudo systemctl status jenkins
# sudo cat /var/lib/jenkins/secrets/initialAdminPassword