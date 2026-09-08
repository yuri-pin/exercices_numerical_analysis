import numpy as np

## Aqui faremos alguns códigos de resolução de sistemas lineares na seguinte ordem:
# 1) Resolução triangular superior
# 2) Resolução triangular inferior unitária 
# 3) Eliminação de Gauss (sem pivotiamento)
# 4) Decomposição LU (sem pivotiamento) 
# 5) Cálculo de Inversa (usando os dois modos)
# 6) Problema mal condicionado


#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

def Solv_U(A, b):
    """Esse código tem como objetivo resolver um sistema triangular superior.
    
    Onde nossas entradas podem ser definidas:
            A : a matriz triangular superior
            b : os termos independentes
    
       Essa função assume que a matriz A já está na formatação correta de forma que seja 
    compatível com b.
    """
    x = np.empty_like(b)
    n = len(b)

    #como criamos um elemento x com empty, temos que determinar o último elemento dele fora do laço
    x[-1] = b[-1]/A[n-1,n-1]

    #agora podemos resolver o restante
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            soma = A[i,j]*x[j]
        x[i] = (b[i]-soma)/A[i,i]

    return x


#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

def Solv_L_uni(A,b):
    """Esse código tem como objetivo resolver um sistema triangular inferioir com diagonal unitária.
    
    Onde nossas entradas podem ser definidas:
            A : a matriz triangular inferior unitária
            b : os termos independentes
    
       Essa função assume que a matriz A já está na formatação correta de forma que seja 
    compatível com b.
    """
    x = np.empty_like(b)
    n = len(b)

    #como criamos um elemento x com empty, temos que determinar o último elemento dele fora do laço
    x[0] = b[0]

    #agora podemos resolver o restante
    for i in range(1,n):
        for j in range(0,i):
            soma = A[i,j]*x[j]
        x[i] = (b[i]-soma)

    return x

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------





M = np.array([[1,0],[2,1]])
c = np.array([1,1])
print(Solv_L_uni(M,c))