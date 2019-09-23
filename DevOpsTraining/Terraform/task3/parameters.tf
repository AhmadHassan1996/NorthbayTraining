variable "s3bucket" {
  type = "map"
  default = {
    "bucket-1" = "ahmad-tf-test-bucket-1"
    "bucket-2" = "ahmad-tf-test-bucket-2"
  }
}