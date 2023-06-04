# EC2 Instance.
resource "aws_instance" "ec2_instance" {
    ami = var.instance_ami
    instance_type = var.instance_type
    vpc_security_group_ids = [aws_security_group.security_group.id]
    key_name = var.public_key_name
    user_data     = file("${path.module}/${var.user_data_file_path}")
    tags = {
      Name = var.instance_name
    }
}

output "ec2_instance_output" {
  value = aws_instance.ec2_instance.id
}