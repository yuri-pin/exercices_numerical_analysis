## Aqui vamos criar algumas matrizes para analisarmos depois com diversos métodos de sistemas lineares
## sendo que pretendemos aplicar a importancia de diferentes decomposições para diferentes problemas.

## Primeiro iremos gerar uma matriz que possui todas as entradas aleatórias, com valores inteiros entre 
## 0 e 100, em uma matriz 100 x 100.

import numpy as np

def random_M():
    A = np.random.randint(0,100,size = (100,100))

    np.save("random_M.npy", A)
    return

def random_v():
    b = np.random.randint(0,100, size = (100))

    np.save("random_v.npy", b)
    return


## Segunda matriz será uma matriz mal condicionada (seja lá o que for isso), para vermos como os resultados 
## são alterados dependendo do tipo de matriz 

def hilbert_M(n):
    H = np.zeros([n,n])
    for i in range(0,n):
        for j in range(0,n):
            H[i,j] = 1/(i+j+1)

    np.save("Hilbert.npy", H)
    return



## Por fim, para o último exemplo teremos a construção de uma matriz tridiagonal, que é definida positiva,
## onde poderemos usar a decomposição de cholesky

def tridiagonal(n):
    T = np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            if abs(i-j)==0:
                T[i,j] = 2
            elif abs(i-j) == 1:
                T[i,j] = -1

    np.save("trigiagonal.npy", T)
    return

## Comentário: para resolver esse tipo de problema específico, podemos usar o algoritmo de thomas, como 
## descrito no link: 
## https://pt.wikipedia.org/wiki/Algoritmo_de_Thomas

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

random_M()
random_v()
hilbert_M(10)
tridiagonal(10)