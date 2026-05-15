#!/usr/bin/env bash
set -euo pipefail

URL="${1:-http://127.0.0.1:8000/health}"
# timeout in seconds for curl
TIMEOUT=5

# call endpoint, require HTTP 200 and JSON body containing "status":"ok"
resp=$(curl -sS --max-time "$TIMEOUT" -w "%{http_code}" -H "Accept: application/json" "$URL")
http_code="${resp: -3}"
body="${resp:0:${#resp}-3}"

if [[ "$http_code" != "200" ]]; then
  echo "ERROR: expected HTTP 200, got $http_code"
  echo "Body: $body"
  exit 2
fi

# Use jq to validate JSON and value (jq required in CI; fallback to grep if absent)
if command -v jq >/dev/null 2>&1; then
  status=$(echo "$body" | jq -r '.status // empty')
  if [[ "$status" != "ok" ]]; then
    echo "ERROR: unexpected status: '$status'"
    echo "Body: $body"
    exit 3
  fi
else
  # simple text match fallback
  if ! echo "$body" | grep -q '"status"[[:space:]]*:[[:space:]]*"ok"'; then
    echo "ERROR: response does not contain \"status\": \"ok\""
    echo "Body: $body"
    exit 4
  fi
fi

echo "Health check OK"