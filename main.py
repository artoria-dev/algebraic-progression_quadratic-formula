import numpy as np

var_limit = 14  # change according to game


def func(a, b, c):
    if a <= 0.5 or b <= 0 or c <= 0:
        return -np.inf
    return (b * c) ** (a / 2 - 0.5)


def constraint(a, b, c):
    return b ** 2 - 4 * a * c >= 0


a_range = range(0, var_limit + 1)
b_range = range(0, var_limit + 1)
c_range = range(0, var_limit + 1)

max_value = -np.inf
max_coords = (0, 0, 0)

for a in a_range:
    for b in b_range:
        for c in c_range:
            if constraint(a, b, c):
                value = func(a, b, c)
                if value > max_value:
                    max_value = value
                    max_coords = (a, b, c)

a_max, b_max, c_max = max_coords
print(f'maximum at: a = {a_max}, b = {b_max}, c = {c_max}')
print(f'maximum value: {max_value:.4f}')
