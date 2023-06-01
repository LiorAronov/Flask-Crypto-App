# Ubuntu Instance for jenkins server.
resource "aws_instance" "jenkins_instance" {
    ami = var.jenkins_instance_ami
    instance_type = var.jenkins_instance_type
    vpc_security_group_ids = [aws_security_group.jenkins_security_group.id]
    key_name = var.public_key_name
    user_data = filebase64("user_data_script.sh")
    tags = {
      Name = var.jenkins_instance_name
    }
}

# IAM user for Jenkins server.
resource "aws_iam_user" "jenkins_user" {
  name = var.jenkins_user_name
  path = "/"
  tags = {
    Name = var.jenkins_user_name
  }
}

# Admin Policy attachment to Jenkins user.
resource "aws_iam_user_policy_attachment" "user_admin_policy" {
  user       = aws_iam_user.jenkins_user.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}

# Generate IAN Access key for Jenkins user.
resource "aws_iam_access_key" "user_access_key" {
  user = aws_iam_user.jenkins_user.name
}

# pull Access key and Access ID to keys/txt.file.
resource "local_file" "jenkins_user_key_file" {
  filename = "../../keys/${var.jenkins_user_name}_keys.txt"
  content = "AWS_ACCESS_KEY_ID: ${aws_iam_access_key.user_access_key.id} \nAWS_SECRET_ACCESS_KEY: ${aws_iam_access_key.user_access_key.secret}"

}