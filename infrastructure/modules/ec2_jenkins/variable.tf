# The instance module variables.
variable "jenkins_instance_name" {
    type = string
}

variable "jenkins_instance_ami" {
    type = string
}

variable "jenkins_instance_type" {
    type = string
}

variable "public_key_name" {
    type = string
}

# The security group module variables.
variable "jenkins_security_group_name" {
    type = string
}

variable "jenkins_user_name" {
    type = string
}