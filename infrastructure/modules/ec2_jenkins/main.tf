# EC2 Instance.
resource "aws_instance" "jenkins_instance" {
    ami = var.jenkins_instance_ami
    instance_type = var.jenkins_instance_type
    vpc_security_group_ids = [aws_security_group.jenkins_security_group.id]
    key_name = var.public_key_name
    # user_data     = file("user_data.sh")

    tags = {
      Name = var.jenkins_instance_name
    }
}

resource "aws_iam_user" "jenkins_user" {
  name = var.jenkins_user_name
  path = "/"
  
  tags = {
    Name = var.jenkins_user_name
  }
}
  

resource "aws_iam_access_key" "jenkins_user_access_key" {
  user = aws_iam_user.jenkins_user.name
}

resource "aws_iam_user_policy_attachment" "jenkins_user_admin_policy" {
  user       = aws_iam_user.jenkins_user.name
  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
}

resource "local_file" "jenkins_user_access_key_file" {
  filename = "../../keys/${var.jenkins_user_name}_keys.txt"
  content = "AWS_ACCESS_KEY_ID: ${aws_iam_access_key.jenkins_user_access_key.id} \nAWS_SECRET_ACCESS_KEY: ${aws_iam_access_key.jenkins_user_access_key.secret}"

}