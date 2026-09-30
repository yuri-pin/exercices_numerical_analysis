import numpy as np 

def F1(x):
    return x**3 - x  - 1

def F2(x):
    return x*np.log10(x) - 1

def derivada(f,x):
    if f is F1:
        return 2*x**2 -1
    elif f is F2:
        return np.log(x) + 1

def intervalo(f):
    if f is F1:
        a = 1
        b = 2
    elif f is F2:
        a = 2 
        b = 3
    return a,b

def phi_MPF(f,x):
    if f is F1:
        return (x+1)**(1/3)
    elif f is F2:
        return x - 1.3*(f(x))