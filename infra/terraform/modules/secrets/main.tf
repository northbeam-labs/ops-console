# secrets module
variable "env" { type = string }

output "secrets_id" { value = "secrets-${var.env}" }
