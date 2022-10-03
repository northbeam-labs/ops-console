# ecr module
variable "env" { type = string }

output "ecr_id" { value = "ecr-${var.env}" }
