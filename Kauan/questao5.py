import numpy as np
import numpy.random as npr
from questao4 import Array_1d_5, Array_1d_6

# Crating a stacked array
Array_stacked = np.hstack((Array_1d_5, Array_1d_6))

print(Array_stacked)
# Stats
mean = np.mean(Array_stacked)
std = np.std(Array_stacked)
variance = np.var(Array_stacked)

# printing the stats
print(f"mean: {mean}")
print(f"standard deviation: {std}")
print(f"variance: {variance}")

transform_impares = Array_stacked%2 == 1
print(transform_impares)
print(Array_stacked[transform_impares])