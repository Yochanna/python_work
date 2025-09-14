# eq_world_map_hover_titles.py
import json
from pathlib import Path
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "browser"  # open in your browser

# --- Safe load: handles BOM and leading whitespace ---
p = Path("data/eq_data_1_day_m1.geojson")
text = p.read_text(encoding="utf-8-sig").lstrip("\ufeff").strip()
if not text or not text.startswith("{"):
    raise ValueError(f"Unexpected content in {p}: first 40 chars -> {repr(text[:40])}")
data = json.loads(text)
features = data["features"]

# Build lists
mags   = [f["properties"]["mag"] for f in features]
lons   = [f["geometry"]["coordinates"][0] for f in features]
lats   = [f["geometry"]["coordinates"][1] for f in features]
titles = [f["properties"]["title"] for f in features]

fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    color=mags,                 # color by magnitude
    hover_name=titles,          # show title on hover
    title="Global Earthquakes (1 Day Feed)",
    projection="natural earth",
)
fig.show()
