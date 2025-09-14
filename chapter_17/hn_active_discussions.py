import requests
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "browser"  # open in your browser

TOP_N = 30           # fetch 30 IDs…
SHOW_N = 15          # …then chart the top 15 by comments

# 1) Get top story IDs
ids = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json", timeout=10).json()

stories = []
for iid in ids[:TOP_N]:
    try:
        d = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{iid}.json", timeout=10).json() or {}
        # Some posts (e.g., promos) can miss keys -> use .get and guard
        title = d.get("title") or "(no title)"
        comments = d.get("descendants")  # total comments
        by = d.get("by") or "(unknown)"

        # If comments is missing, None, or not an int -> skip (as the book hints)
        if not isinstance(comments, int):
            continue

        # Always make the label link to the HN discussion page
        discussion_url = f"https://news.ycombinator.com/item?id={iid}"

        stories.append({
            "title": title,
            "comments": comments,
            "by": by,
            "discussion_url": discussion_url,
        })
    except Exception:
        # If any fetch fails, just skip that item
        continue

# 2) Sort by comments (descending) and keep the top SHOW_N
stories.sort(key=lambda s: s["comments"], reverse=True)
stories = stories[:SHOW_N]

# 3) Build lists for the chart
labels = [f"<a href='{s['discussion_url']}'>{s['title']}</a>" for s in stories]
counts = [s["comments"] for s in stories]
hover  = [f"by {s['by']}" for s in stories]

# 4) Plot
fig = px.bar(
    x=labels, y=counts,
    title="Most Active Hacker News Discussions (by comment count)",
    labels={"x": "Submission (click to open discussion)", "y": "Comments"},
    template="plotly_white",
    hover_name=hover,
)
fig.update_traces(marker_opacity=0.75)
fig.update_xaxes(tickangle=-30, tickfont=dict(size=12))
fig.update_yaxes(tickfont=dict(size=12))
fig.update_layout(title_font_size=22, margin=dict(l=60, r=30, t=60, b=120))

fig.show()
