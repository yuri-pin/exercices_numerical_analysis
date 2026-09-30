import numpy as np 
import função as func
import metodos as met
from prettytable import PrettyTable



funci = (func.F1, func.F2)
meto = (met.bissecao,met.pos_falsa,met.MPF, met.Newton,met.secante)
metodo =("Bisseção","Posição Falsa", "MPF", "Newton", "Secante")
for f in funci:
    
    a, b = func.intervalo(f)

    tol = 10**-6

    # Cria a tabela
    tabela = PrettyTable()

    # Define os cabeçalhos das colunas
    tabela.field_names = ["Método Usado", "Iteração", "x_c", "f(x_c)"]

    for i in range(len(metodo)):
        x_bar,f_bar,j = meto[i](a = a,b = b,f = f,tol = tol)
        # Adiciona as linhas com os dados
        tabela.add_row([metodo[i],j, x_bar, f_bar])
        

    # Imprime a tabela formatada
    print(tabela)
