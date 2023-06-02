# The ec2_instance module variables.
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
variable "user_data_script" {
    type = string
}

variable "elastic_ip_name" {
    type = string
}

variable "security_group_name" {
    type = string

}