# ecs module
variable "env" { type = string }

output "ecs_id" { value = "ecs-${var.env}" }
