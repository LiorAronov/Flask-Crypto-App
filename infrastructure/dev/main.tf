# Launch tf-state module.
module "tf-state_module" {
    source = "../modules/tf-state"
    remote_state_bucket_name = var.remote_state_bucket_name
    locking_state_table_name = var.locking_state_table_name
}

# Launch ec2/key_pair module.
module "key_pair_module" {
    source = "../modules/ec2/key_pair"
    public_key_pair_name = var.public_key_name
    private_key_pair_name = "${var.private_key_name}.pem"
}

# Launch ec2 module.
module "ec2_module" {
    source = "../modules/ec2_build"
    depends_on = [
        module.key_pair_module
    ]

    instance_name = var.instance_name
    instance_ami = var.instance_ami
    instance_type = var.instance_type
    public_key_name = var.public_key_name
    security_group_name = var.security_group_name
    elastic_ip_name = var.elastic_ip_name
}

 module "route53_module" {
    source = "../modules/route53"
     depends_on = [
        module.ec2_build_module
        ]

    domain_address = var.domain_address
    elastic_ip_public = module.ec2_module.elastic_ip_data
}



