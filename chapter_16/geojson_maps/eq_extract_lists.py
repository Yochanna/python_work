import json
from pathlib import Path

# Safe read: handles BOM if present
text = Path('data/eq_data_1_day_m1.geojson').read_text(encoding='utf-8-sig').lstrip('\ufeff')
data = json.loads(text)
features = data['features']

mags   = [f['properties']['mag'] for f in features]
lons   = [f['geometry']['coordinates'][0] for f in features]
lats   = [f['geometry']['coordinates'][1] for f in features]
titles = [f['properties']['title'] for f in features]

print("mags:", mags[:5])
print("lons:", lons[:5])
print("lats:", lats[:5])
print("titles:", titles[:2])
