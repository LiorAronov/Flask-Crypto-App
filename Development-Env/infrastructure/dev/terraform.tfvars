# Variable value.
remote_state_name = "remote-state-flask-crypto-app"
locking_state_name = "locking-state-flask-crypto-app"

public_key_name = "public-terrform-key"
private_key_name = "private-terrform-key"

jenkins_security_group_name = "jenkins-security-group" 
jenkins_security_group_description = ""
jenkins_ingress_rules = ""
jenkins_egress_rules = ""
jenkins_instance_name = "jenkins-instance"
jenkins_instance_ami  = "ami-053b0d53c279acc90" #Ubuntu
jenkins_instance_type = "t2.micro"
jenkins_user_data_script = file("${path.module}/user_data/jenkins_user_data_script.sh")
jenkins_elastic_ip_name = "jenkins-elastic-ip"

jenkins_user_name = "jenkins-user"
jenkins_user_policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"

app_security_group_name = "app-security-group"
app_security_group_description = ""
app_ingress_rules = []
app_egress_rules = ""
app_instance_name = "app-instance"
app_instance_ami = "ami-04581fbf744a7d11f" #Linux
app_instance_type = "t2.micro"
app_user_data_script = file("${path.module}/user_data/app_user_data_script.sh")
app_elastic_ip_name = "app-elastic-ip"

domain_address = "lioraronov.com" #Pravite Domain Address.