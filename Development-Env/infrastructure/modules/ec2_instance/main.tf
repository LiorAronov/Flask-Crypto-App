# EC2 Instance.
resource "aws_instance" "ec2_instance" {
    ami = var.instance_ami
    instance_type = var.instance_type
    vpc_security_group_ids = [aws_security_group.security_group.id]
    key_name = var.public_key_name
    user_data = var.user_data_script
    tags = {
      Name = var.instance_name
    }
}

# Elastic Ip.
resource "aws_eip" "elastic_ip" {
    vpc   = true
    domain = "vpc"    
    instance = aws_instance.ec2_instance.id
    tags = {
        Name = var.elastic_ip_name
    }
}

output "elastic_ip_output" {
  value = aws_eip.elastic_ip.public_ip
}

