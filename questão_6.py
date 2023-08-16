import numpy as np
import numpy.random as npr

def questão_6():
    vetor1 = np.array([[1,2,3],[8,7,5]])
    vetor2 = np.array([[4,5,6],[2,5,3]])

    produtovetorial = np.cross(vetor1, vetor2)

    print("O resultado do produto dos dois vetores é:\n",produtovetorial)

