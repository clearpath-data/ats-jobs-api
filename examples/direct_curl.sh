#!/usr/bin/env bash
# Free, no account: count open jobs on each public ATS endpoint (needs curl + jq).
set -euo pipefail
echo "greenhouse/stripe: $(curl -sS https://boards-api.greenhouse.io/v1/boards/stripe/jobs | jq '.jobs | length')"
echo "lever/spotify:     $(curl -sS 'https://api.lever.co/v0/postings/spotify?mode=json' | jq 'length')"
echo "ashby/openai:      $(curl -sS https://api.ashbyhq.com/posting-api/job-board/openai | jq '.jobs | length')"
