# ats-jobs-api

Pull open jobs from **Greenhouse, Lever and Ashby** job boards with Python or curl, and normalize them into one schema. There are two ways to do it:

1. **Free, no account:** call each ATS's public job-board JSON endpoint directly (`examples/direct_*.py|sh`).
2. **One call for six ATSs** (Greenhouse, Lever, Ashby, Workable, SmartRecruiters, Recruitee): use the Apify Actor [ats-jobs-by-company](https://apify.com/clearpath-data/ats-jobs-by-company) (`examples/actor_*.py|sh`).

> **Disclosure:** I built and sell the ats-jobs-by-company Actor ($0.001 per saved job on Apify's free plan). Option 1 needs nothing from me.

**Tutorial:** [Watching a company's hiring week to week: snapshot and diff Greenhouse, Lever and Ashby job boards](https://dev.to/clearpathdata/watching-a-companys-hiring-week-to-week-snapshot-and-diff-greenhouse-lever-and-ashby-job-boards-1gk7) on dev.to.

## The public endpoints
| ATS | Endpoint | Jobs are in | Title | Location | URL | Date |
|---|---|---|---|---|---|---|
| Greenhouse | `https://boards-api.greenhouse.io/v1/boards/{slug}/jobs` | `.jobs` | `title` | `location.name` | `absolute_url` | `updated_at` (ISO) |
| Lever | `https://api.lever.co/v0/postings/{slug}?mode=json` | top-level list | `text` | `categories.location` | `hostedUrl` | `createdAt` (epoch ms) |
| Ashby | `https://api.ashbyhq.com/posting-api/job-board/{slug}` | `.jobs` | `title` | `location` | `jobUrl` | `publishedAt` (ISO) |

The slug is the board name in the careers URL (`jobs.lever.co/spotify` → `spotify`). Endpoints checked with live requests on 2026-10-19.

## Quick start
```bash
pip install -r requirements.txt

# Free: direct endpoints
python examples/direct_boards.py      # normalizes all three into one list
bash   examples/direct_curl.sh        # job counts per board (needs jq)

# Actor: one schema, six ATSs (needs an Apify account; free tier available)
export APIFY_TOKEN=...                # from https://console.apify.com/settings/integrations
python examples/actor_python.py
bash   examples/actor_curl.sh         # capped with maxTotalChargeUsd=0.05
```

## Track hiring changes (snapshot + diff)
```bash
cd examples/hiring_diff
python snapshot.py lever spotify          # writes snapshots/lever-spotify-<date>.json
# ...a day or more later...
python snapshot.py lever spotify
python diff.py snapshots/<older>.json snapshots/<newer>.json   # opened / closed postings
python actor_new_since.py                 # Actor: jobs posted in the last 7 days (needs APIFY_TOKEN)
```

## Real output (2026-10-19)
`examples/direct_curl.sh`:
```
greenhouse/stripe: 729
lever/spotify:     82
ashby/openai:      814
```
`examples/direct_boards.py`:
```
1625 jobs
greenhouse | stripe | Abuse Investigator | Dublin
lever | spotify | Art Director - Mexico | Mexico City
ashby | openai | Technical Program Manager, Compute Infrastructure | San Francisco
```
`examples/actor_python.py`:
```
Stripe | greenhouse | Project Manager, Total Rewards | CHI, ATL, US-REM
Stripe | greenhouse | Indirect Tax Advisory Consultant | SEA, SF, NYC
Stripe | greenhouse | Solutions Engineer, AI Build Team | US-SF, US-NYC, US-Remote
```
Job titles and counts change daily.

## Notes
- Your token is read only from the `APIFY_TOKEN` environment variable. Never commit it (`.env` is git-ignored).
- These are companies' public career feeds. Cache results and don't poll more often than you need.

## License
MIT
