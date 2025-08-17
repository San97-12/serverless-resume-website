variable "bucket_name" {
  type        = string
  description = "The name of the S3 bucket used for static site hosting"
}

variable "aws_region" {
  type        = string
  description = "The AWS region to deploy resources in"
  default     = "us-east-1" 
}
