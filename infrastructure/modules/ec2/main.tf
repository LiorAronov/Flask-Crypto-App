# EC2 Instance.
resource "aws_instance" "main_instance" {
    ami = var.instance_ami
    instance_type = var.instance_type
    vpc_security_group_ids = [aws_security_group.security_group.id]
    key_name = var.public_key_name
    tags = {
      Name = var.instance_name
    }
}  


# Elastic Ip.
resource "aws_eip" "elastic_ip_flask_application" {
  vpc = true
  instance = aws_instance.main_instance.id
    tags = {
        Name = var.elastic_ip_name
    }

}

