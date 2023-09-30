import random as ram

#tanteo
def tanteo_(fx):
    x= ram.randint (-1000,1000)
    contador=0
    while True:
        fx_a = fx.replace("x",str(x))
        contador+=1
        if (eval(fx)) <0:
            aux=x + 0.2
            x=aux
        elif (eval(fx))>0:
            aux=x-0.2
            x=aux
        if abs(eval(fx))<=0.001:break
    return x,contador


#biseccion
def biseccion_(fx):
    x_1= ram.randint(0,1000)
    x_2= ram.randint(-1000,0)
    contador=0
    while True:
        fx_b= fx.replace("x",str(x_1))
        fx_b_=fx.replace("x",str(x_2))
        if (eval(fx_b))>0 and (eval(fx_b_))<0:
            c= (x_1+x_2)/2
            contador+=1
            fc= fx.replace("x",str(c))
            if abs(eval(fc))<=0.001:break
            else:
                if(eval(fc))>0:
                    x_1= c
                if (eval(fc))<0:
                    x_2= c      
        else:
            x_1= ram.randint(0,1000)
            x_2= ram.randint(-1000,0)
    return x_1,contador
 
print(biseccion_("2*x-8"))

#regla falsa
def regla_falsa_(fx):
    x_1= ram.randint(0,1000)
    x_2= ram.randint(-1000,0)
    contador=0
    while True:
        fx_r= fx.replace("x",str(x_1))
        fx_rf=fx.replace("x",str(x_2))
        if (eval(fx_r))>0 and (eval(fx_rf))<0:
            c= x_1-(eval(fx_r)*(x_2-x_1))/((eval(fx_rf)-(eval(fx_r))))
            contador+=1
            fc_= fx.replace("x",str(c))
            if abs(eval(fc_))<=0.001:break   
            else:
                if(eval(fc_))>0:
                    x_1= c
                if (eval(fc_))<0:
                    x_2=c      
        else:
            x_1= ram.randint(0,1000)
            x_2= ram.randint(-1000,0)
    return c, contador
print (regla_falsa_("2*x-8"))
