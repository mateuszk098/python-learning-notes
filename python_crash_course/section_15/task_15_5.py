'''
Simple random walk representation with matplotlib.
'''

import random

import matplotlib.pyplot as plt


class RandomWalk():
    ''' Represents random walk. '''

    def __init__(self, number_of_tries: int) -> None:
        self.number_of_tries: int = number_of_tries

        # Initial point has x = 0 and y = 0 coordinates.
        self.x_values: list[int] = [0]
        self.y_values: list[int] = [0]

    def fill_walk(self) -> None:
        ''' Generates a random walk points in XY space. '''
        while len(self.x_values) < self.number_of_tries:

            x_step: int
            y_step: int
            x_step, y_step = self._get_step()

            if x_step == 0 and y_step == 0:
                continue

            x: int = self.x_values[-1] + x_step
            y: int = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def _get_step(self):
        ''' Generates random step in XY space. '''
        # Choose direction and distance for x.
        # If you remove -1 or 1 then you can generate a noise.
        x_direction: int = random.choice([-1, 1])
        x_distance: int = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        x_step: int = x_direction*x_distance

        y_direction: int = random.choice([-1, 1])
        y_distance: int = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        y_step: int = y_direction*y_distance

        return x_step, y_step


if __name__ == "__main__":

    while True:
        tries_number: int = 50_000
        number_point: range = range(1, tries_number+1)
        rw: RandomWalk = RandomWalk(tries_number)
        rw.fill_walk()

        plt.style.use("seaborn")
        fig, ax = plt.subplots(figsize=(8, 5), dpi=100)
        ax.scatter(rw.x_values, rw.y_values, c=number_point, cmap=plt.cm.Blues, s=2, edgecolor="none")  # type: ignore
        ax.scatter(0, 0, c="red", s=20, edgecolor="none")
        ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", s=20, edgecolor="none")
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
        plt.show()

        running: str = input("Enter 'n' to exit: ")
        if running == "n":
            break
