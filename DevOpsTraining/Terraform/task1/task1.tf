resource "aws_vpc" "main" {
  cidr_block = var.vpc_cb
  enable_dns_hostnames = true
}

resource "aws_subnet" "public_subnet_1" {
  vpc_id     = "${aws_vpc.main.id}"
  cidr_block = var.subnet_cb["public-subnet-1"]
  map_public_ip_on_launch = true
}

resource "aws_subnet" "public_subnet_2" {
  vpc_id     = "${aws_vpc.main.id}"
  cidr_block = var.subnet_cb["public-subnet-2"]
  map_public_ip_on_launch = true
}

resource "aws_subnet" "private_subnet_1" {
  vpc_id     = "${aws_vpc.main.id}"
  cidr_block = var.subnet_cb["private-subnet-1"]
}

resource "aws_subnet" "private_subnet_2" {
  vpc_id     = "${aws_vpc.main.id}"
  cidr_block = var.subnet_cb["private-subnet-2"]
}

resource "aws_security_group" "ahmad_security_group" {
  name        = "ahmad_security_group"
  description = "Allow TLS inbound traffic"
  vpc_id      = "${aws_vpc.main.id}"

  ingress {
    cidr_blocks = ["0.0.0.0/0"]
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
  }
  egress {
	protocol = -1
	from_port = 0 
	to_port = 0 
	cidr_blocks = ["0.0.0.0/0"]
	}
}

