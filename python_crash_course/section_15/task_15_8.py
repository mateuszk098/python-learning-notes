'''
Simple visualization with plotly. Histogram of two 6-sides dies rools multplication.
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
    die1: Die = Die()
    die2: Die = Die()
    max_result: int = die1.num_sides*die2.num_sides

    results: list[int] = []
    for _ in range(100_000):
        result: int = die1.roll()*die2.roll()
        results.append(result)

    frequencies: list[int] = []
    for value in range(1, max_result+1):
        frequency: int = results.count(value)
        frequencies.append(frequency)

    x_values: list[int] = list(range(1, max_result+1))
    data: list[Bar] = [Bar(x=x_values, y=frequencies)]

    x_axis_config: dict[str, str | int] = {"title": "Result", "dtick": 1}
    y_axis_config: dict[str, str] = {"title": "Frequency of Value."}
    ms_layout: Layout = Layout(title="Result of multiplication of two D6 rolls.",
                               xaxis=x_axis_config, yaxis=y_axis_config)

    offline.plot({"data": data, "layout": ms_layout}, filename="mult_d6_d6.html")
