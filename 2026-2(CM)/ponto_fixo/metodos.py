import numpy as np 
import função as func

def bissecao(a,b,f, tol):
    try:
        p = f(a) * f(b)
        if p > 0:
            raise ValueError("Não há garantia de raiz neste intervalo (f(a) * f(b) > 0).")
        elif p == 0:
            print("Um dos extremos é a raiz.")
            return a if f(a) == 0 else b

    except ValueError as e:
        print(f"Erro de entrada: {e}")
        return None
    except Exception as e:
        print(f"Erro ao calcular a função nos pontos iniciais: {e}")
        return None

    
    f_inf = f(a)
    f_sup = f(b)
    i = 1
    while abs(a - b) > tol and abs(f_inf) > tol:
        pm = (a+b)/2
        f_med = f(pm)
        i += 1
        if f_med*f_inf<0:
            b = pm
            f_sup = f_med

        else:
            a = pm
            f_inf = f_med


    return pm, f_med, i


def pos_falsa(a,b,f,tol):
    try:
            p = f(a) * f(b)
            if p > 0:
                raise ValueError("Não há garantia de raiz neste intervalo (f(a) * f(b) > 0).")
            elif p == 0:
                print("Um dos extremos é a raiz.")
                return a if f(a) == 0 else b
    
    except ValueError as e:
        print(f"Erro de entrada: {e}")
        return None
    except Exception as e:
        print(f"Erro ao calcular a função nos pontos iniciais: {e}")
        return None

    f_inf = f(a)
    f_sup = f(b)
    i = 1
    while abs(a - b) > tol and abs(f_inf) > tol:
        x_bar = (a*f_sup - b*f_inf)/(f_sup-f_inf)
        f_bar = f(x_bar)
        i += 1
        if f_bar*f_inf<0:
                b = x_bar
                f_sup = f_bar

        elif f_bar*f_sup < 0:
                a = x_bar
                f_inf = f_bar

    return x_bar, f_bar, i


def MPF (a,b,f,tol):
    x_0 = np.random.uniform(a, b)
    x_1 = func.phi_MPF(f,x_0)

    f_val = f(x_1)
    i = 1
    while abs(x_1 - x_0) > tol and abs(f_val) > tol:
        x_0 = x_1
        x_1 = func.phi_MPF(f,x_0)
        f_val = f(x_1)
        i += 1

    return x_1, f_val, i

def Newton(a,b,f,tol):
    x_0 = np.random.uniform(a,b)
    x_1 = x_0 - f(x_0)/func.derivada(f,x_0)

    f_val = f(x_1)
    i = 1
    while abs(x_1 - x_0) > tol and abs(f_val) > tol:
        x_0 = x_1
        x_1 = x_0 - f(x_0)/func.derivada(f,x_0)
        f_val = f(x_1)
        i += 1

    return x_1, f_val, i

def secante(a,b,f,tol):
    x_m1 = a
    x_0 = b

    f_inf = f(x_m1)
    f_sup = f(x_0)
    i = 1
    while abs(x_m1 - x_0) > tol and abs(f_sup) > tol:
        x_bar = (x_m1*f_sup - x_0*f_inf)/(f_sup-f_inf)
        f_bar = f(x_bar)

        x_m1 = x_0
        x_0 = x_bar
        f_inf = f_sup
        f_sup = f_bar
        i += 1
    
    return x_bar, f_bar, i

