# IAM user.
resource "aws_iam_user" "iam_user" {
  name = var.iam_user_name
  path = "/"
  tags = {
    Name = var.iam_user_name
  }
}

# IAM Policy attachment.
resource "aws_iam_user_policy_attachment" "iam_policy" {
  user       = aws_iam_user.iam_user.name
  policy_arn = var.policy_arn
}

# Generate Access key.
resource "aws_iam_access_key" "iam_access_key" {
  user = aws_iam_user.iam_user.name
}

# pull Access key and Access ID to keys/txt.file.
resource "local_file" "iam_access_key_local" {
  filename = "../../keys/${var.iam_user_name}-keys.txt"
  content = "AWS_ACCESS_KEY_ID: ${aws_iam_access_key.iam_access_key.id} \nAWS_SECRET_ACCESS_KEY: ${aws_iam_access_key.iam_access_key.secret}"

}