import random as rnd
contador=0
def pol(x):return 5*x**2+5*x

x_a= rnd.randint(-100,0)
x_b= x_a*-1

while True:
    contador+=1
    x_c=x_a-((pol(x_a)*(x_a-x_b))/(pol(x_a)-pol(x_b)))

    if abs(pol(x_c))<=0.0001:
        break
    elif pol(x_a)*pol(x_c)<0:
        x_b=x_c;x_c=x_a-((pol(x_a)*(x_a-x_b))/(pol(x_a)-pol(x_b)))
    else:
        x_a=x_c;x_c=x_a-((pol(x_a)*(x_a-x_b))/(pol(x_a)-pol(x_b)))
print('La solución es:',x_c,'encontrada en',contador,'iteraciones')







