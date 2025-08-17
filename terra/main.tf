provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "static_site" {
  bucket = var.bucket_name

  lifecycle {
    prevent_destroy = true
    ignore_changes  = [
      tags,
      website,
      cors_rule,
    ]
  }
}
