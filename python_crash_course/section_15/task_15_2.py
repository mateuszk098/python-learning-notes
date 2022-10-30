'''
Simple plot of cubes.
'''

import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use("seaborn")
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)  # type: ignore
ax.set_title("Numbers' Cubes", fontsize=18)
ax.set_xlabel("Number", fontsize=14)
ax.set_ylabel("Cube", fontsize=14)
ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()
