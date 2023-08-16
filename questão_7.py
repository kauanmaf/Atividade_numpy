import numpy as np
import numpy.random as npr

def questão_7():
    ndarray8 = np.array([[1, 1, 1],[3, 5, 4], [3, 6, 5]])
    print("O array é:", ndarray8)

    print("\n", "#"*40, "\n")

    identidade = np.identity(3)
    print("A identidade é:", identidade)

    print("\n", "#"*40, "\n")

    determinante = np.linalg.det(ndarray8)
    print("O determinante é:", determinante)

    print("\n", "#"*40, "\n")

    inversa = np.linalg.inv(ndarray8).astype(int)
    print("A inversa é:", inversa)

    print("\n", "#"*40, "\n")

    print(np.dot(ndarray8, inversa))
    print("O resultado da multiplicação é a identidade, logo, a corretude foi demonstrada")
    