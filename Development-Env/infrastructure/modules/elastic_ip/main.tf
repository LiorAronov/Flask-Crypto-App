# Elastic Ip.
# resource "aws_eip" "elastic_ip" {
#     instance = var.ec2_instance_id
#     tags = {
#         Name = var.elastic_ip_name
#     }
# }




resource "aws_eip" "elastic_ip" {
  vpc = true
}

resource "aws_eip_association" "apply_elastic_ip" {
  instance_id   = var.ec2_instance_id
  allocation_id = aws_eip.elastic_ip.id
}



output "elastic_ip_output" {
  value = aws_eip.elastic_ip.public_ip
}
