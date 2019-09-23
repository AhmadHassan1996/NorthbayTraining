variable "ami" {
  default = "ami-0b69ea66ff7391e80"
}
variable "instance_type" {
  default = "t2.micro"
}
variable "key_name" {
  default = "ahmad"
}
variable "vpc_id" {}
variable "private_subnet_id" {}
variable "public_subnet_id" {}
variable "vpc_security_group_id" {}
