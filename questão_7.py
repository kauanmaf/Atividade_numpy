import numpy as np
import numpy.random as npr

ndarray8 = np.array([[4, 2, 3],[1, -4, 6], [-2, 3, -1]])
print("O array é:", ndarray8)

print("\n", "#"*40, "\n")

identidade = np.identity(3)
print("A identidade é:", identidade)

print("\n", "#"*40, "\n")

determinante = np.linalg.det(ndarray8)
print("O determinante é:", determinante)

print("\n", "#"*40, "\n")

inversa = np.linalg.inv(ndarray8)
print("A inversa é:", inversa)

print("\n", "#"*40, "\n")

print(np.dot(ndarray8, inversa))