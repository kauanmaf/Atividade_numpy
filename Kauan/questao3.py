import numpy as np
import numpy.random as npr
from questao2 import Array_2d_1

array_2d_2 = np.arange(12)

array_2d_2 = array_2d_2.reshape(4,3)

array_multiplication = Array_2d_1 * array_2d_2

print(array_multiplication)