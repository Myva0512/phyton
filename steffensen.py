import random as rnd
xa= rnd.randint (0,100)
contador=0 
xc=xa
print (xa)
def pol(x):
    return 2*x-8

while True:
    contador=+1

    if abs(pol(xc))<=0.001:break
        
    else:
        xc= xa-((pol(xa)**2)/((pol(xa+pol(xa)))-(pol(xa))))
        xa=xc
print("el resulatado es:",xa, "y el numero de iteraciones es:",contador)