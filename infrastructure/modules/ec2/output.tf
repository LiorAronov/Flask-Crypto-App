# Output elastic public ip.
output "elastic_ip_address_data" {
  value = aws_eip.elastic_ip_main_instance.public_ip
}