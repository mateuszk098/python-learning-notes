"""
Draws Lorenz Attractor using 4th-order Runge-Kutta numerical algorithm.
"""


import matplotlib.pyplot as plt

SIGMA: float = 10.
RHO: float = 28.
BETA: float = 10. / 3.


def dx(x: float, y: float) -> float:
    return SIGMA * (y - x)


def dy(x: float, y: float, z: float) -> float:
    return x * (RHO - z) - y


def dz(x: float, y: float, z: float) -> float:
    return x * y - BETA * z


def runge_kutta(
        N: int, dt: float, x_0: float, y_0: float, z_0: float, x_list, y_list, z_list) -> None:

    for _ in range(N):

        x_list.append(x_0)
        y_list.append(y_0)
        z_list.append(z_0)

        k1x: float = dx(x_0, y_0) * dt
        k1y: float = dy(x_0, y_0, z_0) * dt
        k1z: float = dz(x_0, y_0, z_0) * dt

        k2x: float = dx(x_0 + 0.5 * k1x, y_0 + 0.5 * k1y) * dt
        k2y: float = dy(x_0 + 0.5 * k1x, y_0 + 0.5 * k1y, z_0 + 0.5 * k1z) * dt
        k2z: float = dz(x_0 + 0.5 * k1x, y_0 + 0.5 * k1y, z_0 + 0.5 * k1z) * dt

        k3x: float = dx(x_0 + 0.5 * k2x, y_0 + 0.5 * k2y) * dt
        k3y: float = dy(x_0 + 0.5 * k2x, y_0 + 0.5 * k2y, z_0 + 0.5 * k2z) * dt
        k3z: float = dz(x_0 + 0.5 * k2x, y_0 + 0.5 * k2y, z_0 + 0.5 * k2z) * dt

        k4x: float = dx(x_0 + k3x, y_0 + k3y) * dt
        k4y: float = dy(x_0 + k3x, y_0 + k3y, z_0 + k3z) * dt
        k4z: float = dz(x_0 + k3x, y_0 + k3y, z_0 + k3z) * dt

        x_0 += (k1x + 2 * k2x + 2 * k3x + k4x) / 6
        y_0 += (k1y + 2 * k2y + 2 * k3y + k4y) / 6
        z_0 += (k1z + 2 * k2z + 2 * k3z + k4z) / 6


def draw_plot(x_list, y_list, z_list) -> None:

    plt.figure(1)
    plt.grid(ls='--')
    plt.plot(x_list, z_list)
    plt.title("Lorenz Attractor")
    plt.xlabel("x")
    plt.ylabel("z")
    plt.show()


if __name__ == "__main__":

    x_0, y_0, z_0 = 1, 1, 25
    x_list: list[float] = []
    y_list: list[float] = []
    z_list: list[float] = []
    N: int = 10_000
    dt: float = 1e-2

    runge_kutta(N, dt, x_0, y_0, z_0, x_list, y_list, z_list)
    draw_plot(x_list, y_list, z_list)
