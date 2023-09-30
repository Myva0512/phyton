import random as rnd
x_1= rnd.randint(0,1000)
x_2= rnd.randint(-1000,0)
contador=0; band = 0;c = 0
print ('random a', x_1)
print('random b', x_2)
while True:
    contador += 1
    if band == 0:
        if (2*x_1**2-5*x_1+2) > 0: band = 0.5
        if (2*x_1**2-5*x_1+2) < 0: band += 0.5
    
    if band == 1: c = (x_1+x_2)/2
    else:
        x_1= rnd.randint(0,1000)
        x_2= rnd.randint(-1000,0)
    if(2*x_1**2-5*x_1+2) > 0: x_1 = c
    if(2*x_1**2-5*x_1+2) < 0: x_2 = c
    if abs((2*x_1**2-5*x_1+2)) <= 0.001: break
    

print(x_1)
 
