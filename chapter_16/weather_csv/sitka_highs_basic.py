from pathlib import Path
import csv

path = Path('weather_data/sitka_weather_07-2021_simple.csv')
rows = path.read_text().splitlines()
reader = csv.reader(rows)

header = next(reader)                      # skip header row with column names
highs = [int(r[4]) for r in reader]       # column 4 = TMAX (daily high)
print("First 10 highs:", highs[:10])
