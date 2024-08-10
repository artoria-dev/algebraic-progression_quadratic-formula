import numpy as np

var_limit = 13  # change according to game


def func(x, y, z):
    if x <= 0.5 or y <= 0 or z <= 0:
        return -np.inf
    return (y * z) ** (x / 2 - 0.5)


def is_valid(x, y, z):
    return y ** 2 - 4 * x * z >= 0


candidates = [
    (x, y, z)
    for x in range(var_limit + 1)
    for y in range(var_limit + 1)
    for z in range(var_limit + 1)
    if is_valid(x, y, z)
]

x_max, y_max, z_max = max(candidates, key=lambda vars: func(*vars))
max_value = func(x_max, y_max, z_max)

print(f'maximum at: a = {x_max}, b = {y_max}, c = {z_max}')
print(f'maximum value: {max_value:.4f}')
