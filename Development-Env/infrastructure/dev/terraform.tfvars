# Variable value.
remote_state_name = "remote-state-flask-crypto-app"
locking_state_name = "locking-state-flask-crypto-app"

public_key_name = "public-terrform-key"
private_key_name = "private-terrform-key"

security_group_name = "security-group" 
jenkins_instance_name = "jenkins-instance"
jenkins_instance_ami  = "ami-053b0d53c279acc90" #Ubuntu
jenkins_instance_type = "t2.micro"
jenkins_user_data_file_script_path = "../../user_data/jenkins_user_data_script.sh"

jenkins_user_name = "jenkins-user"
jenkins_user_policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"

app_security_group_name = "app-security-group" 
app_instance_name = "app-instance"
app_instance_ami = "ami-04581fbf744a7d11f" #Linux
app_instance_type = "t2.micro"
app_user_data_file_script_path = "../../user_data/app_user_data_script.sh"
app_elastic_ip_name = "app-elastic-ip"

domain_address = "lioraronov.com" #Pravite Domain Address.

