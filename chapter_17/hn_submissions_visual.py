
import requests
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"


# Endpoints
top_endpoint = "https://hacker-news.firebaseio.com/v0/topstories.json"
item_endpoint = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Fetch top 30 story IDs
ids = requests.get(top_endpoint, timeout=10).json()[:30]

# Collect story data
stories = []
for i in ids:
    url = item_endpoint.format(i)
    story = requests.get(url, timeout=10).json()
    if story and "descendants" in story:  # skip promos or ads
        stories.append({
            "title": story["title"],
            "comments": story["descendants"],
            "url": f"https://news.ycombinator.com/item?id={i}"
        })

# Sort by number of comments
stories.sort(key=lambda s: s["comments"], reverse=True)

# Build chart
labels = [s["title"][:40] + "..." for s in stories[:10]]
fig = px.bar(
    x=labels,
    y=[s["comments"] for s in stories[:10]],
    labels={"x": "Discussion", "y": "Comments"},
    title="Most Active Hacker News Discussions"
)

# Save + display
fig.write_html("hn_submissions_visual.html")
fig.show()
