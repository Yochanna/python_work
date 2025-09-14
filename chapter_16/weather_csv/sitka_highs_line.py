from pathlib import Path
import csv
import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
reader = csv.reader(path.read_text().splitlines()); next(reader)

highs = [int(r[4]) for r in reader]       # list of daily highs

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(highs, color='red', linewidth=2)

ax.set_title('Sitka Daily Highs — July 2021')
ax.set_ylabel('Temp (F)')
ax.tick_params(labelsize=10)

plt.show()
