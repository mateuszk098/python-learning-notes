import numpy as np


elements: int = 5
a = np.array([1, 2, 3, 4, 5, 6])
b = np.empty(elements + 1)

# Typical way to calculate weird subsums.
# for i in range(1, elements):
#     b[i] = a[i+1] + a[i-1] - a[i]

# Using indices
b = np.array(a[:-2] + a[2:] - a[1:-1])  # type: ignore
print(b)
