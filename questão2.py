import numpy as np
import numpy.random as npr
from questão1 import Array_1d_1, Array_1d_2, Array_1d_3

# Reshape
Array_1d_3 = Array_1d_3.reshape(4,3)

# Tranforming into float
Array_1d_3 = Array_1d_3.astype(np.float32)

# Transpose

Array_transpose = Array_1d_3.T

print(Array_1d_3)
print(Array_transpose)