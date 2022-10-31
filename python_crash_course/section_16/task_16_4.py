'''
Temperature comparison between Stika and Death Valley.
'''

import csv
from datetime import datetime

import matplotlib.pyplot as plt


def get_temperature_dict(filename: str) -> dict[str, list]:
    """ Get tmin, tmax and dates from the csv file. """
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        header: dict[str, int] = {row: index for index, row in enumerate(header_row)}

        tmin_ind: int = header["TMIN"]
        tmax_ind: int = header["TMAX"]
        date_ind: int = header["DATE"]

        highs: list[int] = []
        lows: list[int] = []
        dates: list[datetime] = []

        for row in reader:
            date: datetime = datetime.strptime(row[date_ind], "%Y-%m-%d")
            try:
                high: int = int(row[tmax_ind])
                low: int = int(row[tmin_ind])
            except ValueError:
                print(f"Lack of data for {date}.")
            else:
                highs.append(high)
                dates.append(date)
                lows.append(low)

    return {"highs": highs, "lows": lows, "dates": dates}


sitka_filename: str = "data/sitka_weather_2018_simple.csv"
death_valley_filename: str = "data/death_valley_2018_simple.csv"

sitka_data: dict[str, list] = get_temperature_dict(sitka_filename)
sitka_highs: list[int] = sitka_data["highs"]
sitka_lows: list[int] = sitka_data["lows"]
sitka_dates: list[datetime] = sitka_data["dates"]

dv_data: dict[str, list] = get_temperature_dict(death_valley_filename)
dv_highs: list[int] = dv_data["highs"]
dv_lows: list[int] = dv_data["lows"]
dv_dates: list[datetime] = dv_data["dates"]

plt.style.use("seaborn")
fig, ax = plt.subplots()
fig.autofmt_xdate()

ax.plot(sitka_dates, sitka_highs, c="blue", lw=0.75)
ax.plot(sitka_dates, sitka_lows, c="blue", lw=0.75)
ax.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor="blue", alpha=0.1, label="Sitka")  # type: ignore

ax.plot(dv_dates, dv_highs, c="red", lw=0.75)
ax.plot(dv_dates, dv_lows, c="red", lw=0.75)
ax.fill_between(dv_dates, dv_highs, dv_lows, facecolor="red", alpha=0.1, label="Death Valley")  # type: ignore

ax.set_title("Temperature comparison in 2018.", fontsize=18)
ax.set_xlabel("", fontsize=14)
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.set_ylim(0, 140)
ax.tick_params(axis="both", which="major", labelsize=14)
ax.legend(fontsize=14)

plt.show()
