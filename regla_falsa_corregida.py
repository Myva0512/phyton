import random as rnd
x_1= rnd.randint(0,100)
x_2= rnd.randint(-100,0)
contador=0
print ('random a', x_1)
print('random b', x_2)
while True:
    if (((x_1**8)-256)>0 and ((x_2**8)-256)<0):
        c= (x_1-(((x_1**8)-256)*(x_2-x_1))/(((x_2**8)-256)-((x_1**8)-256)))
        print(c)
        contador= contador+1
        if abs(((c**8)-256))<=0.0001:
            print('la solucion es: ',c)
            print('el numero de iteraiones es: ', contador)
            break   
        else:
            if((c**8)-256)>0:
                x_1= c
            if ((c**8)-256)<0:
                x_2=c      
    else:
        x_1= rnd.randint(0,1000)
        x_2= rnd.randint(-1000,0)