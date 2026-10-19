"""Save today's open jobs for one company board as {job_url: title}."""
import datetime, json, pathlib, sys
import requests

FETCH = {
    "greenhouse": lambda s: [(j["absolute_url"], j["title"]) for j in
        requests.get(f"https://boards-api.greenhouse.io/v1/boards/{s}/jobs", timeout=30).json()["jobs"]],
    "lever": lambda s: [(j["hostedUrl"], j["text"]) for j in
        requests.get(f"https://api.lever.co/v0/postings/{s}", params={"mode": "json"}, timeout=30).json()],
    "ashby": lambda s: [(j["jobUrl"], j["title"]) for j in
        requests.get(f"https://api.ashbyhq.com/posting-api/job-board/{s}", timeout=30).json()["jobs"]],
}

def snapshot(ats, slug, folder="snapshots"):
    jobs = dict(FETCH[ats](slug))
    path = pathlib.Path(folder) / f"{ats}-{slug}-{datetime.date.today()}.json"
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(jobs, indent=1, ensure_ascii=False))
    return path, len(jobs)

if __name__ == "__main__":
    print(*snapshot(sys.argv[1], sys.argv[2]))
