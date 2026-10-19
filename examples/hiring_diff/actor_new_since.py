import os
from apify_client import ApifyClient  # pip install "apify-client>=3"

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("clearpath-data/ats-jobs-by-company").call(run_input={
    "companies": ["https://jobs.lever.co/spotify"],
    "postedSince": "7 days",
    "maxResults": 20,
    "descriptionMode": "none",
})
rows = client.dataset(run.default_dataset_id).list_items().items
print(len(rows), "Spotify jobs posted in the last 7 days")
for r in rows[:3]:
    print(r["postedAt"][:10], "|", r["title"])
