import random as ram
from numpy import inf
from numpy import nan
import matplotlib
matplotlib.use('TkAgg',force=True)
from matplotlib import pyplot as plt

def tanteo_ch(fx,ch):
    if (ch==1):
        contador2=0
        soluciones = []
        tolerancia= 0.001
        while contador2<100:
            x= ram.randint (-10,10)
            contador=0
            while abs(eval(fx.replace("x",str(x))) <tolerancia) or contador<100:
                contador+=1 
                if (eval(fx.replace("x",str(x))) <tolerancia):
                    aux=x + 0.1
                    x=aux
                else:
                    aux=x - 0.1
                    x=aux 
            contador2+=1
            if (round(x, 3)) not in soluciones:
                soluciones.append(round(x, 3))
        return soluciones, contador
   
def biseccion_ch(fx, ch):
    if ch == 1:
        contador2 = 0
        soluciones = []
        tolerancia = 0.001
        while contador2 < 2:
            x_1 = ram.randint(-10, 0)
            x_2 = ram.randint(0, 10)
            contador = 0
            x = (x_1 + x_2) / 2
            while abs(eval(fx.replace("x", str(x)))) > tolerancia and contador < 100:
                contador += 1
                if eval(fx.replace("x", str(x))) < 0:
                    x_1 = x
                else:
                    x_2 = x
                x = (x_1 + x_2) / 2
            contador2 += 1
            if abs(x_2 - x_1) < tolerancia:
                if round(x, 3) not in soluciones:
                    soluciones.append(round(x, 3))
        return soluciones, contador

def regla_ch(fx, ch):
    if ch == 1:
        contador2 = 0
        soluciones = []
        tolerancia = 0.001
        while contador2 < 2:
            x_1 = ram.randint(0, 1000)
            x_2 = ram.randint(-1000, 0)
            contador = 0
            fx_r = fx.replace("x", str(x_1))
            fx_rf = fx.replace("x", str(x_2))
            c = x_1 - eval(fx_r) * (x_2 - x_1) / (eval(fx_rf) - eval(fx_r))
            while abs(eval(fx.replace("x", str(c)))) > tolerancia and contador < 100:
                if eval(fx.replace("x", str(c))) > 0:
                    contador += 1
                    x_1 = c
                    c = x_1 - eval(fx_r) * (x_2 - x_1) / (eval(fx_rf) - eval(fx_r))
                else:
                    x_2 = c
                    c = x_1 - eval(fx_r) * (x_2 - x_1) / (eval(fx_rf) - eval(fx_r))
            contador2 += 1
            if round(c, 3) not in soluciones:
                soluciones.append(round(c, 3))
        return soluciones, contador
 
def newton_ch(fx, ch, derivada):
    if ch == 1:
        contador2 = 0
        soluciones = []
        tolerancia = 0.001
        while contador2 < 2:
            x_0 = ram.randint(-100, 100)
            x_1 = ram.randint(-100, 100)
            contador = 0
            fx_eval = eval(fx.replace("x", str(x_0)))
            fx_eval_d = eval(derivada.replace("x", str(x_0)))
            while fx_eval < tolerancia and contador<100 and fx_eval_d!=0:
                contador += 1
                x_1 = x_0 - (fx_eval / fx_eval_d) 
                fx_eval = eval(fx.replace("x", str(x_1)))
                fx_eval_d = eval(derivada.replace("x", str(x_1)))
                x_0 = x_1
            contador2 += 1
            if round(x_1, 3) not in soluciones:
                soluciones.append(round(x_1, 3))
        return soluciones, contador   

def regla_secante(fx, ch):
    if ch == 1:
        contador2 = 0
        soluciones = []
        tolerancia = 0.001
        while contador2 < 2:
            x_0 = ram.randint(-100, 100)
            x_1 = ram.randint(-100, 100)
            x_a, x_b, x_c = x_0, x_1, x_0
            contador = 0
            while abs(x_1 - x_0) > tolerancia and contador < 100 and len(soluciones) < 2:
                contador += 1
                x_c = x_a - ((eval(fx.replace('x', str(x_a))) * (x_a - x_b)) / (eval(fx.replace('x', str(x_a))) - eval(fx.replace('x', str(x_b)))))
                if abs(eval(fx.replace('x', str(x_c)))) <= 0.0001:
                    if round(x_c, 3) not in soluciones:
                        soluciones.append(round(x_c, 3))
                        x_0, x_1, x_a, x_b = x_1, x_c, x_1, x_c
                else:
                    x_0, x_1, x_a, x_b = x_1, x_c, x_1, x_c
                    
            contador2 += 1
                    
        return soluciones, contador

def steffensen(fx, ch):
    if ch == 1:
        contador2 = 0
        soluciones = []
        tolerancia = 0.001
        while contador2 < 2:
            x_0 = ram.randint(-100, 100)
            x_1 = ram.randint(-100, 100)
            xa, xc = x_0, x_1
            contador = 0
            while abs(eval(fx.replace('x', str(xc)))) > tolerancia and contador < 100:
                contador += 1
                x_c = xa - ((eval(fx.replace('x', str(xa)))) ** 2 / (eval(fx.replace('x', str(xa + eval(fx.replace('x', str(xa)))))) - eval(fx.replace('x', str(xa)))))
                xa = xc
                xc = x_c

            if round(xc, 3) not in soluciones:
                soluciones.append(round(xc, 3))
                if len(soluciones) == 2:
                    break
            contador2 += 1

        return soluciones, contador
