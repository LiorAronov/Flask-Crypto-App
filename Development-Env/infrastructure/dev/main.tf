# Launch tf-state module.
module "tf-state_module" {
    source = "../modules/tf-state"
    remote_state_name = var.remote_state_name
    locking_state_name = var.locking_state_name
}

# Launch key_pair module.
module "key_pair_module" {
    source = "../modules/key_pair"
    public_key_name = var.public_key_name
    private_key_name = var.private_key_name
}

# Launch ec2_jenkins module.
module "ec2_jenkins_module" {
    source = "../modules/ec2_instance"
    depends_on = [
        module.key_pair_module
    ]
    instance_name = var.jenkins_instance_name
    instance_ami = var.jenkins_instance_ami
    instance_type = var.jenkins_instance_type
    public_key_name = var.public_key_name
    user_data_file_path = var.jenkins_user_data_file_script_path
    security_group_name = var.security_group_name
}

# Launch ec2_app module.
module "ec2_app_module" {
    source = "../modules/ec2_instance"
    depends_on = [
        module.key_pair_module
    ]
    instance_name = var.app_instance_name
    instance_ami = var.app_instance_ami
    instance_type = var.app_instance_type
    public_key_name = var.public_key_name
    user_data_file_path = var.app_user_data_file_script_path
    security_group_name = var.app_security_group_name
    }

module "elastic_ip_module" {
    source = "../modules/elastic_ip"
    depends_on = [
        module.ec2_jenkins_module
    ]
    ec2_instance_id = module.ec2_app_module.ec2_instance_output
    elastic_ip_name = var.app_elastic_ip_name

}

# Launch iam_user module.
 module "iam_user_module" {
    source = "../modules/iam_user"
     depends_on = [
        module.ec2_app_module
        ]

    iam_user_name = var.jenkins_user_name
    policy_arn = var.jenkins_user_policy_arn
}

# Launch route53 module.
 module "route53_module" {
    source = "../modules/route53"
     depends_on = [
        module.elastic_ip_module
        ]

    domain_address = var.domain_address
    elastic_ip_public = module.elastic_ip_module.elastic_ip_output
}

