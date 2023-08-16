import numpy as np
from questao_4 import *

# empilhamento horizontal
array_7 = np.hstack((array_5, array_6))

# atribuindo menos a impares e 1 a pares
for index in range(array_7.size):
    if (array_7[index] % 2) != 0:
        array_7[index] = -1
    if (array_7[index] % 2) == 0:
        array_7[index] = 1

def prints_questao_5():
    # estatísticas do array 7
    print("Média: ", np.average(array_7))
    print("Desvio padrão: ", np.std(array_7))
    print("Variância ", np.var(array_7))