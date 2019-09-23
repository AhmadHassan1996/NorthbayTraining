variable "vpc_cb"{
  default = "10.0.0.0/16"
}
variable "subnet_cb"{
  type = "map"
  default = {
    "public-subnet-1" = "10.0.1.0/24"
    "public-subnet-2" = "10.0.2.0/24"
    "private-subnet-1" = "10.0.3.0/24"
    "private-subnet-2" = "10.0.4.0/24"
  }
}