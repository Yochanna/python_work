from pathlib import Path
import csv
import plotly.express as px

rows = list(csv.DictReader(Path('data/world_fires_7_day.csv').read_text(encoding='utf-8-sig').splitlines()))


rows = list(csv.reader(Path('data/world_fires_7_day.csv').read_text().splitlines()))
header, data = rows[0], rows[1:]

lats = [float(r[0]) for r in data]
lons = [float(r[1]) for r in data]
brightness = [float(r[2]) for r in data]

fig = px.scatter_geo(
    lat=lats, lon=lons, size=brightness, color=brightness,
    color_continuous_scale='Hot',
    title='World Fires — past 7 days',
    projection='natural earth'
)
fig.show()
