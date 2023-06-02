# # The modules variables.


variable "remote_state_name" { 
  type        = string
}
variable "locking_state_name" { 
  type        = string
}
variable "public_key_name" { 
  type        = string
}
variable "private_key_name" { 
  type        = string
}
variable "security_group_name" { 
  type        = string
}

variable "jenkins_instance_name" { 
  type        = string
}
variable "jenkins_instance_ami" { 
  type        = string
}
variable "jenkins_instance_type" { 
  type        = string
}
variable "app_security_group_name" { 
  type        = string
}
variable "jenkins_elastic_ip_name" { 
  type        = string
}
variable "jenkins_user_name" { 
  type        = string
}
variable "jenkins_user_policy_arn" { 
  type        = string
}
variable "app_instance_name" { 
  type        = string
}
variable "app_instance_ami" { 
  type        = string
}
variable "app_instance_type" { 
  type        = string
}

variable "app_elastic_ip_name" { 
  type        = string
}
variable "domain_address" { 
  type        = string
}

