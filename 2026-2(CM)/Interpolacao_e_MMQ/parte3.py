import numpy as np

## Como queremos ajustar uma curva para a formula de Arrhenius que é dada por 
##                  k(T) = A_0 exp_{-E_a/(RT)}
## Mas ajustar exponencias de jorma direta, não é tão trivial, dessa forma,  tomaremos o log 
##dessa expressão, obtendo a seguinte expressão:
##                 ln(K) = ln(A_0) - (E_a/R)(1/T)
##                   y   =   a     +   b    * x


## Esses abaixo são os dados que obtivemos
T = np.array([
    290.0, 300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0,
    390.0, 400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0
])

k = np.array([
    4.12e-15, 7.35e-15, 1.28e-14, 2.15e-14, 3.52e-14, 5.64e-14, 8.85e-14, 1.36e-13, 2.04e-13, 3.01e-13,
    4.38e-13, 6.25e-13, 8.78e-13, 1.21e-12, 1.65e-12, 2.22e-12, 2.94e-12, 3.86e-12, 5.01e-12, 6.44e-12
])

## Podemos gerar a matriz A, que é associada ao termo ln(A_0) e ao inverso da temperatura, e o termo 
## independente associado ao ln(k)

A = np.ones((len(T),2))
A[:,1] = 1/T[:]

Y = np.log(k)


## Agora, precisamos determinar qual o sistema normal
##   A^T@A(a,b) = A^T @y

M_normal = np.transpose(A)@A
y_normal = np.transpose(A)@Y

x = np.linalg.solve(M_normal, y_normal)


# Por Fim, temos que voltar para o sistema original que estavamos trabalhando e lembrar que R = 8.314

E_a = -x[1]*8.314

A_0 = np.exp(x[0])

print(A_0, E_a)