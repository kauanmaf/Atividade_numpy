import numpy as np
import numpy.random as npr

# arrays com inteiros aleatórios
array_5 = npr.randint(100, size = 50)
array_6 = npr.randint(100, size = 50)

# função que encontra todos os elementos presentes em ambos os arrays
numeros_comuns, indices_a1, indices_a2 = np.intersect1d(array_5, array_6, return_indices = True)

def prints_questao_4():
    # todos os valores na interseção
    print("Numeros presentes nos dois arrays: ", numeros_comuns)
    # indices no array_5
    print("Indices dos numeros no array 1: ", indices_a1)
    # indices no array_6
    print("Indices dos numeros no array 2: ", indices_a2)

    # printando elementos do array 5 que não estão no 6 na mão
    for index in range(array_5.size):
        for index_2 in range(indices_a1.size):
            if array_5[index] == array_6[index_2]:
                eh_comum = True
            else:
                eh_comum = False
            
        if(eh_comum):
            continue
        print(array_5[index], end=" ")