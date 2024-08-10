import numpy as np

var_limit = 15  # change according to game


def func(a, b, c):
    if a <= 0.5 or b <= 0 or c <= 0:
        return -np.inf
    return (b * c) ** (a / 2 - 0.5)


def is_valid(a, b, c):
    return b ** 2 - 4 * a * c >= 0


candidates = [
    (a, b, c)
    for a in range(var_limit + 1)
    for b in range(var_limit + 1)
    for c in range(var_limit + 1)
    if is_valid(a, b, c)
]

a_max, b_max, c_max = max(candidates, key=lambda vars: func(*vars))
max_value = func(a_max, b_max, c_max)

print(f'maximum at: a = {a_max}, b = {b_max}, c = {c_max}')
print(f'maximum value: {max_value:.4f}')
