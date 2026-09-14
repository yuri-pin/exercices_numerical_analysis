## Aqui vamos criar algumas matrizes para analisarmos depois com diversos métodos de sistemas lineares
## sendo que pretendemos aplicar a importancia de diferentes decomposições para diferentes problemas.

## Primeiro iremos gerar uma matriz que possui todas as entradas aleatórias, com valores inteiros entre 
## 0 e 100, em uma matriz 100 x 100.

import numpy as np

def random_M(n):
    A = np.random.randint(1,10*n,size = (n,n))

    np.save("random_M.npy", A)
    return A

def random_v(n):
    b = np.random.randint(1,10*n, size = (n))

    np.save("random_v.npy", b)
    return b


## Segunda matriz será uma matriz mal condicionada (seja lá o que for isso), para vermos como os resultados 
## são alterados dependendo do tipo de matriz 

def hilbert_M(n):
    H = np.zeros([n,n])
    for i in range(0,n):
        for j in range(0,n):
            H[i,j] = 1/(i+j+1)

    np.save("Hilbert.npy", H)
    return H

def hilbert_v(n):
    h = np.zeros(n)
    for i in range(0,n):
        soma = 0
        for j in range(0,n):
            soma += 1/(i+j+1)
        h[i] = soma
    return h

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
    return T

## Comentário: para resolver esse tipo de problema específico, podemos usar o algoritmo de thomas, como 
## descrito no link: 
## https://pt.wikipedia.org/wiki/Algoritmo_de_Thomas



## construiremos uma matriz definida positiva que não esparça

def gram_schmidt(A):
  # A é uma matriz onde cada coluna é um vetor
  Q = np.zeros_like(A, dtype=float)
  for j in range(A.shape[1]):
    v = A[:, j]
    for i in range(j):
      # Subtrai a projeção nos vetores anteriores já ortonormalizados
      v = v - np.dot(Q[:, i], A[:, j]) * Q[:, i]
    # Normalização
    norm = np.linalg.norm(v)
    if norm > 1e-10:
      Q[:, j] = v / norm
    else:
      Q[:, j] = np.zeros_like(v)
  return Q

def diag_positiva(n):
    D = np.zeros([n,n])
    b = np.random.randint(1,10*n, size = (n))
    for i in range(0,n):
        D[i,i] = b[i]

    return D 

def diag_geral(n):
    D = np.zeros([n,n])
    b = np.random.randint(-10*n,10*n, size = (n))
    for i in range(0,n):
        D[i,i] = b[i]    
    return D


def SDP(n):
    A = random_M(n)
    P = gram_schmidt(A)
    Pt = np.transpose(P)
    D = diag_positiva(n)

    SPD = P@D@Pt

    return SPD


def nSDP(n):
    A = random_M(n)
    P = gram_schmidt(A)
    Pt = np.transpose(P)
    D = diag_geral(n)

    nSPD = P@D@Pt
    return nSPD    




#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

def permuta_linha(M,i, j):
    N =np.copy(M) 
    N[[i,j]] = N[[j,i]]
    return N
    