# Data Source - Hosted Zones.
data "aws_route53_zone" "hosted_zones" {
  name = var.domain_address
}

# # Data Source - Elastic Ip Address ID.
data "aws_eip" "elastic_ip_address_data" {
  public_ip = var.elastic_ip_public

}
