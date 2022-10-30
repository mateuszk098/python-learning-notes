'''
Simple visualization with plotly. Histogram of two 8-sides dies rools.
'''

import random

from plotly.graph_objects import Bar, Layout
from plotly import offline


class Die():
    def __init__(self, num_sides: int = 6) -> None:
        self.num_sides: int = num_sides

    def roll(self) -> int:
        return random.randint(1, self.num_sides)


if __name__ == '__main__':
    die1: Die = Die(8)
    die2: Die = Die(8)
    max_result: int = die1.num_sides + die2.num_sides

    results: list[int] = [die1.roll() + die2.roll() for _ in range(10_000)]
    frequencies: list[int] = [results.count(value) for value in range(2, max_result+1)]

    x_values: list[int] = list(range(2, max_result+1))
    data: list[Bar] = [Bar(x=x_values, y=frequencies)]

    x_axis_config: dict[str, str | int] = {"title": "Result", "dtick": 1}
    y_axis_config: dict[str, str] = {"title": "Frequency of Value."}
    ms_layout: Layout = Layout(title="Result of sum of two D8 rolls.", xaxis=x_axis_config, yaxis=y_axis_config)

    offline.plot({"data": data, "layout": ms_layout}, filename="d8_d8.html")
