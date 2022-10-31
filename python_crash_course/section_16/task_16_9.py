'''
World fires with plotly.
'''

import csv

from plotly.graph_objects import Layout
from plotly import offline

filename: str = "data/world_fires_1_day.csv"
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    lats: list[float] = []
    lons: list[float] = []
    brightness: list[float] = []

    for row in reader:
        try:
            lat: float = float(row[0])
            lon: float = float(row[1])
            bright: float = float(row[2])
        except ValueError:
            print(f"Lack of data.")
        else:
            lats.append(lat)
            lons.append(lon)
            brightness.append(bright)

data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "marker": {
        "size": [0.05*bright for bright in brightness],
        "color": brightness,
        "colorscale": "Viridis",
        "reversescale": True,
        "colorbar": {"title": "Brightness"}
    }, }]

my_layout = Layout(title="World fires, last day")

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="world_fires.html")
