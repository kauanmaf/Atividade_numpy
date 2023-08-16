import numpy as np
import numpy.random as npr
from questao1 import Array_1d_3

# Reshape
Array_2d_1 = Array_1d_3.reshape(4,3)

# Tranforming into float
Array_2d_1 = Array_2d_1.astype(np.float32)

# Transpose
Array_transpose = Array_2d_1.T