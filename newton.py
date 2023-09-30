import random as rnd 
x_0= rnd.randint(-100,100)
contador=0
print(x_0)
while True:
    contador +=1
    if abs(5*x_0**2+5*x_0)<=0.001:
        print ("la respuesta es ",x_0,"el nuemro de iteraciones es", contador)
        break
    else:
        x_1= x_0 -(5*x_0**2+5*x_0) / (10*x_0+5)
        x_0=x_1
