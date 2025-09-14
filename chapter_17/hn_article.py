import requests
import json  # just to pretty-print

# 1) Pick one known story id (any valid HN id works)
item_id = 31353677
url = f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"

# 2) Make the request
r = requests.get(url, timeout=10)
print("Status code:", r.status_code)      # 200 = OK

# 3) Convert JSON to Python dict
item_dict = r.json()

# 4) See the shape (keys) and a neat preview
print("Keys on the item:", list(item_dict.keys()))
print("\nFirst 400 chars of the item (pretty):")
print(json.dumps(item_dict, indent=2)[:400])
