# route53 module
variable "env" { type = string }

output "route53_id" { value = "route53-${var.env}" }
