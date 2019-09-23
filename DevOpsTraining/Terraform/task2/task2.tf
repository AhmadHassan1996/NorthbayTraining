provider "aws" {
  profile    = "default"
  region     = "us-east-1"
}

resource "aws_internet_gateway" "internet_gateway" {
  vpc_id = var.vpc_id
}

resource "aws_route_table" "route_table" {
  vpc_id = var.vpc_id
}

resource "aws_route" "route" {
  route_table_id        = "${aws_route_table.route_table.id}"
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = "${aws_internet_gateway.internet_gateway.id}"
}

resource "aws_route_table_association" "route_table_association" {
  subnet_id      = var.public_subnet_id
  route_table_id = "${aws_route_table.route_table.id}"
}

resource "aws_security_group" "ahmad_security_group_1" {
  name        = "ahmad_security_group_1"
  description = "Allow TLS inbound traffic"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["10.0.2.0/24"]
  }
}

resource "aws_instance" "ahmad-tf-instance" {
  ami           = var.ami
  instance_type = var.instance_type
  subnet_id = var.private_subnet_id
  associate_public_ip_address = false
  vpc_security_group_ids = ["${aws_security_group.ahmad_security_group_1.id}"]
  key_name = var.key_name
  
  tags = {
    Name = "ahmad_tf_instance"
  }
}

resource "aws_instance" "ahmad-tf-bastion-host" {
  ami           = var.ami
  instance_type = var.instance_type
  subnet_id = var.public_subnet_id
  associate_public_ip_address = true
  vpc_security_group_ids = [var.vpc_security_group_id]
  key_name = var.key_name

  tags = {
    Name = "ahmad_tf_bastion_host"
  }
}
