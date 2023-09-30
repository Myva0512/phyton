import random as rnd
x_0= rnd.randint(0,100)

if abs(((3*x_0)-27)) <=0.001:
    print ('la respuesta es:', x_0)
else:
     contador=0
     while True:
        x_1= x_0-0.2
        x_0=x_1
        contador=contador+1
        if abs(((3*x_0)-27)) <=0.001:
            print ('la respuesta es:', x_0)
            print ('el numero de iteraciones es:', contador)
            break
        