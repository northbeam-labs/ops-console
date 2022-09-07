# alb module
variable "env" { type = string }

output "alb_id" { value = "alb-${var.env}" }
