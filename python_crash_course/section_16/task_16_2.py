'''
Simple matplotlib visualization from csv file.
'''

import csv
from datetime import datetime

import matplotlib.pyplot as plt


filename: str = "data/death_valley_2018_simple.csv"
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs: list[int] = []
    lows: list[int] = []
    dates: list[datetime] = []

    for row in reader:
        date: datetime = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            high: int = int(row[4])
            low: int = int(row[5])
        except ValueError:
            print(f"Lack of data for {date}.")
        else:
            highs.append(high)
            dates.append(date)
            lows.append(low)

plt.style.use("seaborn")
fig, ax = plt.subplots()
fig.autofmt_xdate()

ax.plot(dates, highs, c="red", lw=0.75)
ax.plot(dates, lows, c="blue", lw=0.75)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)  # type: ignore
ax.set_title("Highest temperature during the day in 2018.", fontsize=18)
ax.set_xlabel("", fontsize=14)
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.set_ylim(0, 140)
ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()
