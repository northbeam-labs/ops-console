# rds module
variable "env" { type = string }

output "rds_id" { value = "rds-${var.env}" }
