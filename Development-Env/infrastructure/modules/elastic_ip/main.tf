# Elastic Ip.
resource "aws_eip" "elastic_ip" {
    instance = var.ec2_instance_id
    tags = {
        Name = var.elastic_ip_name
    }
}

output "elastic_ip_output" {
  value = aws_eip.elastic_ip.public_ip
}
