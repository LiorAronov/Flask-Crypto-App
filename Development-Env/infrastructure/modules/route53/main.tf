# Routing to Registered Domain.
resource "aws_route53_record" "routing_to_domain" {
    zone_id = data.aws_route53_zone.hosted_zones.id
    name    = var.domain_address
    type    = "A"
    ttl = 300
    records = [data.aws_eip.elastic_ip_address_data.public_ip]
}