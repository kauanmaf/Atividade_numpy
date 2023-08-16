import numpy as np
import numpy.random as npr
from questao2 import Array_2d_1

Array_1d_5 = npr.randint(0,20,12)
Array_1d_6 = npr.randint(0,40,12)

# Comum elements
intersection = np.intersect1d(Array_1d_5, Array_1d_6)
print(intersection)

# Index
Indexs = np.intersect1d(Array_1d_5, Array_1d_6, return_indices= True) 
print(Indexs)

# Differences
diferences = np.setdiff1d(Array_1d_5, Array_1d_6)
print(diferences)