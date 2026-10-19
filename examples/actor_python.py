import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
INPUT = {"companies": ["stripe"], "maxResults": 3, "descriptionMode": "none"}
run = client.actor("clearpath-data/ats-jobs-by-company").call(run_input=INPUT)
rows = client.dataset(run.default_dataset_id).list_items().items
for r in rows:
    print(r["company"], "|", r["ats"], "|", r["title"], "|", r["location"])
