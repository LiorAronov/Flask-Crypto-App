# The instance module variables.
variable "instance_name" {
    type = string
}

variable "instance_ami" {
    type = string
}

variable "instance_type" {
    type = string
}

variable "public_key_name" {
    type = string
}

# The security group module variables.
variable "security_group_name" {
    type = string
}

# The elastic ip module variables.
variable "elastic_ip_name" {
    type = string
}



