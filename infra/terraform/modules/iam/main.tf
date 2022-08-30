# iam module
variable "env" { type = string }

output "iam_id" { value = "iam-${var.env}" }
