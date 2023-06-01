# RSA Algorithm Key.
resource "tls_private_key" "rsa" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

# Public key - store in AWS vonsole.
resource "aws_key_pair" "public_terrform_key" {
  key_name   = var.public_key_pair_name
  public_key = tls_private_key.rsa.public_key_openssh
}

# Private key - store in local file.
resource "local_file" "private_terrform_key" {
  content  = tls_private_key.rsa.private_key_pem
  filename = "../../../private_terrform_key/${var.private_key_pair_name}.pem"  
}
