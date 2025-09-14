from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

def read_series(csv_path):
    reader = csv.reader(Path(csv_path).read_text().splitlines()); next(reader)
    d, hi, lo = [], [], []
    for r in reader:
        try:
            d.append(datetime.strptime(r[2], "%Y-%m-%d"))
            hi.append(int(r[4])); lo.append(int(r[5]))
        except Exception:
            continue
    return d, hi, lo

d1, h1, l1 = read_series('weather_data/sitka_weather_07-2021_simple.csv')
d2, h2, l2 = read_series('weather_data/death_valley_2018_simple.csv')

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(d1, h1, 'r-', alpha=0.8, label='Sitka highs')
ax.plot(d2, h2, 'k-', alpha=0.6, label='Death Valley highs')

ax.set_title('Highs: Sitka vs Death Valley')
ax.set_ylabel('Temp (F)')
ax.legend()
fig.autofmt_xdate()
plt.show()
