'''
Simple matplotlib visualization from csv file.
'''

import csv
from datetime import datetime

import matplotlib.pyplot as plt


filename: str = "data/sitka_weather_2018_simple.csv"
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    prcps: list[float] = []
    dates: list[datetime] = []

    for row in reader:
        date: datetime = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            prcp: float = float(row[3])
        except ValueError:
            print(f"Lack of data for {date}.")
        else:
            prcps.append(prcp)
            dates.append(date)

plt.style.use("seaborn")
fig, ax = plt.subplots()
fig.autofmt_xdate()

ax.plot(dates, prcps, c="blue", lw=0.75)
ax.set_title("Average rainfall during the day in 2018.", fontsize=18)
ax.set_xlabel("", fontsize=14)
ax.set_ylabel("PRCP (mm)", fontsize=14)
ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()
