import random as ram
x= ram.randint (-1000,1000)
print("el numero es:", x)
contador=0
if abs(((3*x)-27))<=0.001:
    print ("la respuesta es: ",x)
else:
    while True:
        contador= contador +1
        if ((3*x)-27) <0:
            aux=x + 0.2
            x=aux
        elif ((3*x)-27)>0:
            aux=x-0.2
            x=aux
        if abs(((3*x)-27))<=0.001:
            print ("la respuesta es: ",x)
            print ("el numero de iteraciones es: ", contador)
            break