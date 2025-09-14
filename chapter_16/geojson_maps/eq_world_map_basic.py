import json
from pathlib import Path
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "browser"

text = Path('data/eq_data_1_day_m1.geojson').read_text(encoding='utf-8-sig')
data = json.loads(text)
features = data['features']

mags = [f['properties']['mag'] for f in features]
lons = [f['geometry']['coordinates'][0] for f in features]
lats = [f['geometry']['coordinates'][1] for f in features]

fig = px.scatter_geo(lat=lats, lon=lons, size=mags,
                     title="Global Earthquakes (1 Day Feed)",
                     projection="natural earth")
fig.show()
