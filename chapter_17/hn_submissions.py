import requests

# 1) Get a list of "top" story IDs
top_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(top_url, timeout=10)
print("Status code (topstories):", r.status_code)

id_list = r.json()           # a plain Python list of integers (story IDs)
print("How many IDs did we get?", len(id_list))

# 2) Take a small slice so we don't spam the API while learning
top_n = 10
ids_to_fetch = id_list[:top_n]

# 3) Fetch each story and gather a tiny summary
stories = []
for iid in ids_to_fetch:
    item_url = f"https://hacker-news.firebaseio.com/v0/item/{iid}.json"
    ir = requests.get(item_url, timeout=10)
    if ir.status_code != 200:
        print(f"  Skipping {iid} (status {ir.status_code})")
        continue

    d = ir.json() or {}
    # Choose safe defaults with dict.get to avoid KeyError if a field is missing
    stories.append({
        "title": d.get("title", "(no title)"),
        "by": d.get("by", "(unknown)"),
        "score": d.get("score", 0),
        "url": d.get("url", "(no link)"),
        "id": d.get("id", iid),
    })

# 4) Sort by score (highest first)
stories.sort(key=lambda s: s["score"], reverse=True)

# 5) Print a neat summary
print(f"\nTop {len(stories)} Hacker News stories (by score):")
for s in stories:
    print(f"• {s['title']} — ↑{s['score']} — by {s['by']}")
    print(f"  {s['url']}")
