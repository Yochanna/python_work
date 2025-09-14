import json
from pathlib import Path

# read text allowing BOM; strip any leading BOM just in case
p = Path('data/eq_data_1_day_m1.geojson')
text = p.read_text(encoding='utf-8-sig').lstrip('\ufeff')
data = json.loads(text)
features = data['features']

print('features:', len(features))
print('first feature keys:', list(features[0].keys()))
print('properties keys:', list(features[0]['properties'].keys()))
print('geometry keys:', list(features[0]['geometry'].keys()))


