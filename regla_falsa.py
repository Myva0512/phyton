import random as rnd
x_1= rnd.randint(0,1000)
x_2= rnd.randint(-1000,0)
contador=0
print ('random a', x_1)
print('random b', x_2)
while True:
    if (((8*x_1)-10)>0 and ((8*x_2)-10)<0):
        c= (x_1-(((8*x_1)-10)*(x_2-x_1))/(((8*x_2)-10)-((8*x_1)-10)))
        contador= contador+1
        if abs(((8*c)-10))<=0.0001:
            print('la solucion es: ',c)
            print('el numero de iteraiones es: ', contador)
            break   
        else:
            if((2*c)-11)>0:
                x_1= c
            if ((2*c)-11)<0:
                x_2=c  
    else:
        x_1= rnd.randint(0,1000)
        x_2= rnd.randint(-1000,0)