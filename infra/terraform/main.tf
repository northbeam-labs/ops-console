terraform {
  required_providers {
    aws = { source = "hashicorp/aws" }
  }
}

provider "aws" {
  region = var.region
}

module "vpc" {
  source = "./modules/vpc"
  env    = var.env
}
module "ecs" {
  source = "./modules/ecs"
  env    = var.env
}
module "rds" {
  source = "./modules/rds"
  env    = var.env
}
module "s3" {
  source = "./modules/s3"
  env    = var.env
}
module "iam" {
  source = "./modules/iam"
  env    = var.env
}
module "alb" {
  source = "./modules/alb"
  env    = var.env
}
module "route53" {
  source = "./modules/route53"
  env    = var.env
}
module "ecr" {
  source = "./modules/ecr"
  env    = var.env
}
module "cloudwatch" {
  source = "./modules/cloudwatch"
  env    = var.env
}
module "secrets" {
  source = "./modules/secrets"
  env    = var.env
}
