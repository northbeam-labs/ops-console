# cloudwatch module
variable "env" { type = string }

output "cloudwatch_id" { value = "cloudwatch-${var.env}" }
