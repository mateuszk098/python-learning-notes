'''
Simple matplotlib visualization from csv file.
'''

import csv
from datetime import datetime

import matplotlib.pyplot as plt


filename: str = "data/vostok_2021.csv"
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    temps: list[float] = []
    dates: list[datetime] = []

    for row in reader:
        print(row[2])
        date: datetime = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            temp: float = float(row[5])
        except ValueError:
            print(f"Lack of data for {date}.")
        else:
            temps.append(temp)
            dates.append(date)

plt.style.use("seaborn")
fig, ax = plt.subplots()
fig.autofmt_xdate()

ax.plot(dates, temps, c="red", lw=0.75)
ax.set_title("Average temperature at Vostok Station in 2021.", fontsize=18)
ax.set_xlabel("", fontsize=14)
ax.set_ylabel("Temperature (C)", fontsize=14)
ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()
