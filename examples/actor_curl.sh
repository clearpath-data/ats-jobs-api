#!/usr/bin/env bash
# Run the ats-jobs-by-company Actor and print the jobs as JSON.
# Requires: export APIFY_TOKEN=...  (https://console.apify.com/settings/integrations)
set -euo pipefail
: "${APIFY_TOKEN:?Set APIFY_TOKEN first}"
curl -sS -X POST \
  "https://api.apify.com/v2/acts/clearpath-data~ats-jobs-by-company/run-sync-get-dataset-items?maxTotalChargeUsd=0.05" \
  -H "Authorization: Bearer ${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"companies": ["stripe"], "maxResults": 3, "descriptionMode": "none"}'
