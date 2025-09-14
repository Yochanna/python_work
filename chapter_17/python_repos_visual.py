# chapter_17/python_repos_visual.py
import requests
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "browser"  # force browser output

# 1) GitHub API call
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print("Status code:", r.status_code)
response_dict = r.json()
repo_dicts = response_dict["items"]

# 2) Collect fields for top 10 repos
names, stars, urls, owners, descriptions = [], [], [], [], []
for repo in repo_dicts[:10]:
    names.append(repo["name"])
    stars.append(repo["stargazers_count"])
    urls.append(repo["html_url"])
    owners.append(repo["owner"]["login"])
    descriptions.append(repo["description"] or "")

# 3) Build clickable labels and hover texts
link_labels = [f"<a href='{u}'>{n}</a>" for n, u in zip(names, urls)]
hover_texts = [f"{o}<br />{d}" for o, d in zip(owners, descriptions)]

# 4) Chart with clickable links and hover info
fig = px.bar(
    x=link_labels,
    y=stars,
    title="Most-Starred Python Projects on GitHub",
    labels={"x": "Repository", "y": "Stars"},
    template="plotly_white",
    hover_name=hover_texts,
)

# 5) Style tweaks (same as before)
fig.update_traces(marker_color="SteelBlue", marker_opacity=0.75)
fig.update_layout(
    title_font_size=24,
    xaxis_title_font_size=16,
    yaxis_title_font_size=16,
    margin=dict(l=60, r=30, t=60, b=120),
)
fig.update_xaxes(tickangle=-35, tickfont=dict(size=12))
fig.update_yaxes(tickfont=dict(size=12))

fig.show()
