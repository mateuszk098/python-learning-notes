""" 
Fit function to real data from arduino. 
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from scipy.optimize import curve_fit


def function(t, a, c) -> float:
    return c * np.exp(-a*t)


if __name__ == "__main__":

    # Real data
    data = pd.read_csv("time_constant.csv")
    # Masking only one period
    mask = (data["Time (s)"] > 0.000488) & (data["Time (s)"] < 0.000723)
    data = data[mask]
    x_data = data["Time (s)"]
    y_data = data["Channel 1 (V)"]

    # Fit for the parameters a, c of the function
    popt, pcov = curve_fit(function, x_data, y_data)

    # Plotting
    plt.style.use("bmh")
    figure(figsize=(6, 4), dpi=100)
    plt.plot(x_data, y_data, color="blue", label="Data", alpha=0.75)

    # Fit
    plt.plot(
        x_data, function(x_data, *popt),
        linestyle="--", color="red",
        label="Fit: c * exp(-a * t) \n a = %.1f, c = %.1f \n u(a) = %.1f, u(c) = %.1f" %
        tuple(np.append(popt, np.sqrt(np.diag(pcov)))))

    plt.title("Time constant - Fit", fontname="Times New Roman")
    plt.xlabel("Time (s)", fontname="Times New Roman")
    plt.ylabel("Channel 1 (V)", fontname="Times New Roman")
    plt.legend()
    plt.show()
