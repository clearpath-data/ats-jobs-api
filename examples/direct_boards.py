import requests

def greenhouse(slug):
    r = requests.get(f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs", timeout=30)
    r.raise_for_status()
    return [{"ats": "greenhouse", "company": slug, "title": j["title"],
             "location": (j.get("location") or {}).get("name"),
             "url": j["absolute_url"], "updated": j.get("updated_at")}
            for j in r.json()["jobs"]]

def lever(slug):
    r = requests.get(f"https://api.lever.co/v0/postings/{slug}", params={"mode": "json"}, timeout=30)
    r.raise_for_status()
    return [{"ats": "lever", "company": slug, "title": j["text"],
             "location": (j.get("categories") or {}).get("location"),
             "url": j["hostedUrl"], "updated": j.get("createdAt")}  # createdAt is epoch ms
            for j in r.json()]

def ashby(slug):
    r = requests.get(f"https://api.ashbyhq.com/posting-api/job-board/{slug}", timeout=30)
    r.raise_for_status()
    return [{"ats": "ashby", "company": slug, "title": j["title"],
             "location": j.get("location"), "url": j["jobUrl"], "updated": j.get("publishedAt")}
            for j in r.json()["jobs"]]

jobs = greenhouse("stripe") + lever("spotify") + ashby("openai")
print(len(jobs), "jobs")
for ats in ("greenhouse", "lever", "ashby"):
    j = next(x for x in jobs if x["ats"] == ats)
    print(j["ats"], "|", j["company"], "|", j["title"], "|", j["location"])
