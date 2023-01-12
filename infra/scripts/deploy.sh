#!/usr/bin/env bash
set -euo pipefail
for d in k8s/*/; do kubectl apply -f "$d"; done
