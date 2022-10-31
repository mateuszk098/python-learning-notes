'''
Earthquakes visualization with plotly.
'''

import json

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

filename: str = "data/eq_data_7_day_m1.json"
with open(filename, 'r') as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]

mags: list[float] = []
lons: list[float] = []
lats: list[float] = []
hover_texts: list[str] = []

for eq_dict in all_eq_dicts:
    mags.append(eq_dict["properties"]["mag"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])
    hover_texts.append(eq_dict["properties"]["title"])

data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "text": hover_texts,
    "marker": {
        "size": [5*mag for mag in mags],
        "color": mags,
        "colorscale": "Viridis",
        "reversescale": True,
        "colorbar": {"title": "Strength"}
    }, }]

plot_title: str = all_eq_data["metadata"]["title"]
my_layout = Layout(title=plot_title)

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_earthquakes.html")
