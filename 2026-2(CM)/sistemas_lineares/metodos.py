import numpy as np
import time
import gerador as ger

## Aqui faremos alguns códigos de resolução de sistemas lineares na seguinte ordem:
# 1) Resolução triangular superior
# 2) Resolução triangular inferior unitária 
# 3) Eliminação de Gauss (sem pivotiamento)
# 4) Decomposição LU (sem pivotiamento) 
# 5) Cálculo de Inversa (usando os dois modos)
# 6) Problema mal condicionado


#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#1) Resolução da matriz triangular superior 


def Solv_U(A, b):
    """Esse código tem como objetivo resolver um sistema triangular superior.
    
    Onde nossas entradas podem ser definidas:
            A : a matriz triangular superior
            b : os termos independentes
    
       Essa função assume que a matriz A já está na formatação correta de forma que seja 
    compatível com b.
    """
    x = np.empty_like(b, dtype = float)
    n = len(b)

    #como criamos um elemento x com empty, temos que determinar o último elemento dele fora do laço
    x[-1] = b[-1]/A[n-1,n-1]

    #agora podemos resolver o restante
    for i in range(n-2,-1,-1):
        soma = 0
        for j in range(i+1,n):
            soma += A[i,j]*x[j]
        x[i] = (b[i]-soma)/A[i,i]

    return x


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#2) Resolução da matriz triangular inferior unitária 

def Solv_L_uni(A,b):
    """Esse código tem como objetivo resolver um sistema triangular inferioir com diagonal unitária.
    
    Onde nossas entradas podem ser definidas:
            A : a matriz triangular inferior unitária
            b : os termos independentes
    
       Essa função assume que a matriz A já está na formatação correta de forma que seja 
    compatível com b.
    """
    x = np.empty_like(b, dtype = float)
    n = len(b)

    #como criamos um elemento x com empty, temos que determinar o último elemento dele fora do laço
    x[0] = b[0]

    #agora podemos resolver o restante
    for i in range(1,n):
        soma = 0
        for j in range(0,i):
            soma += A[i,j]*x[j]
        x[i] = (b[i]-soma)

    return x

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#3)Resolução de sistemas lineares (Eliminação de Gauss - sem permutação)

def gauss(A,b):
    """Esse código tem como objetivo resolver um sistema linear.
        
        Onde nossas entradas podem ser definidas:
                A : a matriz 
                b : os termos independentes
        
           Essa função assume que a matriz A já está na formatação correta de forma que seja 
        compatível com b.
    """
    n = len(b)
    A_memory = np.copy(A)
    b_memory = np.copy(b)
    for i in range(n-1):
        if A_memory[i,i] ==0:
            print("pivo nulo") #  erifica se o pivô é nulo
            break

        for j in range(i + 1, n):
            fator = A_memory[j, i] / A_memory[i, i] # ele não sendo nulo, calculamos o fator entre o pivô e o próximo indice a ser anulado

            A_memory[j] = A_memory[j] - fator*A_memory[i] # operação entre as linhas da matriz
            b_memory[j] = b_memory[j] - fator*b_memory[i]

    # no final dessa operação essa matriz é triangular inferior
    # Assim, podemos chamar a função 
    x = Solv_U(A_memory,b_memory)
    return x

#---------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#4)Resolução de sistemas lineares (decomposição LU - sem permutação)

def LU(M):

    n = M.shape[0]
    L = np.eye(n, dtype = float)
    U = np.array(M, dtype=float).copy()

    for i in range(n-1):
        if U[i, i] == 0:
            print("pivô nulo")
            break

        for j in range(i + 1, n):
            fator = U[j, i] / U[i, i]
            
            # O fator da eliminação é armazenado diretamente na matriz L
            L[j, i] = fator
            
            # Atualiza os elementos da linha i da matriz U
            U[j, i:] -= fator * U[i, i:]

    return L,U

def Solver_LU(M,b):
    L,U = LU(M)

    y = Solv_L_uni(L,b)
    x = Solv_U(U,y)
    return x


#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
#5)Resolução de sistemas lineares (decomposição LU - sem permutação)

def inversa_gauss(M):

    n = M.shape[0]
    I = np.eye(n, dtype = float)

    inversa = np.empty_like(M, dtype = float)
    for i in range(n):
        inversa[:,i] = gauss(M,I[:,i])

    return inversa

def inversa_LU(M):

    n = M.shape[0]
    I = np.eye(n, dtype = float)

    inversa = np.empty_like(M, dtype = float)
    L,U = LU(M)
    for i in range(n):
        y = Solv_L_uni(L,I[:,i])
        inversa[:,i] = Solv_U(U,y)

    return inversa


#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#6) Resolução de um problema mal condiacionado 
'''
M = ger.hilbert_M(13)
c = ger.hilbert_v(13)

N = ger.permuta_linha(M,0,1)
d = ger.permuta_linha(c,0,1)

print(gauss(N,d))

print(Solver_LU(M,c))
'''

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#6) Decomposição de Cholesky 

def cholesky(A):

    inicio = time.perf_counter()
    B = np.copy(A)
    n = A.shape[0]
    L = np.zeros((n, n), dtype=float)

    for i in range(n):
        for j in range(i + 1):
            # Produto escalar das linhas i e j até a coluna j-1
            soma = np.dot(L[i, :j], L[j, :j])
            
            if i == j:
                val = B[i, i] - soma
                if val <= 0:
                    raise ValueError("A matriz não é definida positiva.")
                L[i, j] = np.sqrt(val)
            else:
                L[i, j] = (B[i, j] - soma) / L[j, j]

    fim = time.perf_counter()
    tempo = fim-inicio
    return L,tempo


A_original = ger.nSDP(2000)
L,tempo1 = cholesky(A_original)
print(tempo1)

inicio2 = time.perf_counter()
D,_ = np.linalg.eig(A_original)
fim2 = time.perf_counter()
print(fim2 - inicio2)