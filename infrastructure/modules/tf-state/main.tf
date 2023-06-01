# S3 Bucket - remote state file.
resource "aws_s3_bucket" "tf_remote_state" {
    bucket = var.remote_state_bucket_name
}

# Enable versioning - s3 state bucket.
resource "aws_s3_bucket_versioning" "tf_s3_versioning" {
    bucket = aws_s3_bucket.tf_remote_state.id
    versioning_configuration {
        status = "Enabled"
        }
}

# dynamodb Table - locking state.
resource "aws_dynamodb_table" "tf_locking_state" {
    name = var.locking_state_table_name
    billing_mode = "PAY_PER_REQUEST"
    hash_key = "LockID"
    attribute {
        name = "LockID"
        type = "S"
        }
}

