from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('weather_data/death_valley_2018_simple.csv')
reader = csv.reader(path.read_text().splitlines()); next(reader)

dates, highs, lows = [], [], []
for r in reader:
    try:
        date = datetime.strptime(r[2], "%Y-%m-%d")
        high = int(r[4]); low = int(r[5])
    except Exception:
        # if a row is broken/empty, we just skip it
        continue
    else:
        dates.append(date); highs.append(high); lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows,  color='blue')
ax.fill_between(dates, lows, highs, facecolor='orange', alpha=0.08)

ax.set_title('Death Valley Highs/Lows (skipping missing data)')
ax.set_ylabel('Temp (F)')
fig.autofmt_xdate()
plt.show()
