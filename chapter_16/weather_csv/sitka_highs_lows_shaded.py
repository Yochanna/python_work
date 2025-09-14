from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
reader = csv.reader(path.read_text().splitlines()); next(reader)

dates, highs, lows = [], [], []
for r in reader:
    try:
        dates.append(datetime.strptime(r[2], "%Y-%m-%d"))  # DATE text → datetime
        highs.append(int(r[4]))                            # TMAX
        lows.append(int(r[5]))                             # TMIN
    except Exception:
        continue

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows,  color='blue')
ax.fill_between(dates, lows, highs, facecolor='blue', alpha=0.1)

ax.set_title('Sitka Highs & Lows — July 2021')
ax.set_ylabel('Temp (F)')
fig.autofmt_xdate()  # tilt dates

plt.show()
