import math

import numpy as np

A0 = 0.5


def An(n):
    return 2 * np.sin(math.pi * n / 2) / (n * math.pi)


def F(eps, time, k, c, R):
    n = 1
    while True:
        G = (c * pow(R, 2) * np.exp(-(k * time * n) / (c * pow(R, 2)))) / (math.pi * pow(n, 2) * k * time)
        if G < eps:
            break
        n = n + 1
    return n


def U(x, t, b, k, c, R):
    u = A0
    a = math.sqrt(k / c)
    for i in range(1, b + 1):
        u += An(i) * np.cos(i * x / R) * np.exp(-pow(i * a / R, 2) * t)

    return u


def get_analutical(k, c, R, T, X_value, x_array, t_array, eps):
    y1 = [U(_x_array, T, F(eps, T, k, c, R), k, c, R) for _x_array in x_array]
    y2 = [U(X_value, _t_array, F(eps, T, k, c, R), k, c, R) for _t_array in t_array]
    return y1, y2
