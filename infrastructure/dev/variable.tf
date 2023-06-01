# The modules variables.

variable "remote_state_bucket_name" { 
  type        = string
}
variable "locking_state_table_name" { 
  type        = string
}

variable "public_key_name" { 
  type        = string
}
variable "private_key_name" { 
  type        = string
}

variable "instance_name" { 
  type        = string
}

variable "instance_ami" { 
  type        = string
}

variable "instance_type" { 
  type        = string
}

variable "security_group_name" { 
  type        = string
}

variable "elastic_ip_name" { 
  type        = string
}

variable "domain_address" { 
  type        = string
}
