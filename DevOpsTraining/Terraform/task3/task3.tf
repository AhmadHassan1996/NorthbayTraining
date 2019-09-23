provider "aws" {
  profile    = "default"
  region     = "us-east-1"
}

resource "aws_s3_bucket" "bucket-1" {
  bucket = var.s3bucket["bucket-1"]
  acl    = "private"
}

resource "aws_s3_bucket" "bucket-2" {
  bucket = var.s3bucket["bucket-2"]
  acl    = "private"
}
