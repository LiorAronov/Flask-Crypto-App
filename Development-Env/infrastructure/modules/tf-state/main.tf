# S3 Bucket - remote state file.
resource "aws_s3_bucket" "s3_state" {
    bucket = var.remote_state_name
}

# Enable versioning - s3 state bucket.
resource "aws_s3_bucket_versioning" "s3_versioning" {
    bucket = aws_s3_bucket.s3_state.id
    versioning_configuration {
        status = "Enabled"
        }
}

# dynamodb Table - locking state.
resource "aws_dynamodb_table" "db_state" {
    name = var.locking_state_name
    billing_mode = "PAY_PER_REQUEST"
    hash_key = "LockID"
    attribute {
        name = "LockID"
        type = "S"
        }
}

