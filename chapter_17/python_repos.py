# chapter_17/python_repos.py
import requests

# 1) Build the search URL: Python repos, sorted by stars
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars"

# 2) Recommended header for GitHub's v3 API
headers = {"Accept": "application/vnd.github.v3+json"}

# 3) Make the request (ask the "waiter")
r = requests.get(url, headers=headers)

# 4) Check if the kitchen said "OK"
print("Status code:", r.status_code)  # 200 = OK

# 5) Turn JSON text → Python dict
response_dict = r.json()

# 6) Peek at the top-level structure
print("Top-level keys:", list(response_dict.keys()))

# 7) Quick counts
print("Total repositories:", response_dict["total_count"])
print("Has item list?:", "items" in response_dict)

# 8) Pull the list of repo dicts
repo_dicts = response_dict["items"]
print("Repositories returned in this page:", len(repo_dicts))

# 9) Peek inside the first repo to see what fields exist
first_repo = repo_dicts[0]
print("Number of fields on first repo:", len(first_repo))
print("Sample field names:", list(first_repo.keys())[:15])

# 10) Human-friendly summary for top 5 repos
print("\nTop 5 repos (name/owner/stars/url/description)")
for repo in repo_dicts[:5]:
    name = repo["name"]
    owner = repo["owner"]["login"]
    stars = repo["stargazers_count"]
    url = repo["html_url"]
    desc = repo["description"]
    print(f"- {name} by {owner} — ⭐ {stars} — {url}")
    print(f"  {desc}\n")
