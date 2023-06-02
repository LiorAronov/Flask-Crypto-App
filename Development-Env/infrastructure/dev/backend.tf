# Setting remote and locking state.

terraform {
  backend "s3" {
    bucket = "remote-state-flask-crypto-app"
    key = "state-flask-crypto-app/terraform.tfstate"
    region = "us-east-1"
    dynamodb_table = "locking-state-flask-crypto-app"
    encrypt = true
  }
}
