import tkinter as TK
import matplotlib.pyplot as plt
import numpy as np
import seleccionador_checkbox as sc

#creacion de la ventana
ventana = TK.Tk()

#anchor de la ventana
ventana.geometry ('1000x1000')

#titulo de la ventana
ventana.title("Metodos Numericos")

#imagen fondo 
ventana.config(bg="gray")
imagen_fondo=TK.PhotoImage(file='Sin título-1.png')
labelimg=TK.Label(ventana,image=imagen_fondo)
labelimg.pack()

#titulo de la pagina con sus respectivas indicaciones
Label_titulo = TK.Label(ventana,text=" Soluciones de metodos numericos ", font= ("Arial Black",20),background="black",fg= "gold")
Label_titulo.place(x=500,y=15,anchor= "center")

#indicaciones al usuario y configuracion
Label_ecuacion = TK.Label(ventana,text=" ingrese la ecuacion ", font= ("Arial",12),background="black",fg= "gold")
Label_ecuacion.place(x=250,y=75,anchor= "center")

#lo que ingresa el usuario y configuracion
ecuacion= TK.StringVar()
Txtbox_ingreso= TK.Entry(ventana, background= "black", fg="white", font= ("Arial",14),textvariable=ecuacion)
Txtbox_ingreso.place(x=280,y=75,anchor= "center")


#seleccion checkbox
def calcular():
    if (tanteo.get()==1):
        respuesta,contador= sc.tanteo_ch(Txtbox_ingreso.get())
        label_soluciontanteo["text"]="la respuesta de tanteo es: " + str(respuesta) +  " \n y iteraciones:"   +str(contador)

    if (biseccion.get()==1):
        respuesta,contador= sc.biseccion_ch(Txtbox_ingreso.get())
        label_solucionbiseccion["text"]="la respuesta de bisecion es: " + str(respuesta) +  " \n y iteraciones:"   +str(contador)

    if (regla_falsa.get()==1):
        respuesta,contador= sc.regla_falsa_ch(Txtbox_ingreso.get())
        label_solucionregla["text"]="la respuesta de regla falsa es: " + str(respuesta) +  " \n y iteraciones:"   +str(contador)

    if (tanteo.get()==1 & biseccion.get()==1):
        respuesta,contador= sc.tanteo_ch(Txtbox_ingreso.get())
        respuesta2,contador2= sc.biseccion_ch(Txtbox_ingreso.get())
        label_soluciontanteo["text"]+="la respuesta por tanteo es: " + str(respuesta) +  " \n y iteraciones:"   +str(contador) 
        label_solucionbiseccion["text"]+="la respuesta por biseccion es: " + str(respuesta2) + "\n y iteraciones:" + str(contador2)

    if (tanteo.get()==1 & regla_falsa.get()==1):
        respuesta,contador= sc.tanteo_ch(Txtbox_ingreso.get())
        respuesta2,contador2= sc.regla_falsa_ch(Txtbox_ingreso.get())
        label_soluciontanteo["text"]+="la respuesta por tanteo es: " + str(respuesta) +  " \n y iteraciones:"  +str(contador)
        label_solucionregla["text"]+= "la respuesta por regla falsa es: " + str(respuesta2) + "\n y iteraciones:" + str(contador2)
    
    if (biseccion.get()==1 & regla_falsa.get()==1):
        respuesta,contador= sc.biseccion_ch(Txtbox_ingreso.get())
        respuesta2,contador2= sc.regla_falsa_ch(Txtbox_ingreso.get())
        label_solucionbiseccion["text"]+="la respuesta por biseccion es: " + str(respuesta) +  " \n y iteraciones:"   +str(contador)
        label_solucionregla["text"]+="la respuesta por regla falsa es: " + str(respuesta2) + "\n y iteraciones:" + str(contador2)
    
    if (biseccion.get()==1 & regla_falsa.get()==1 & tanteo.get()==1):
        respuesta,contador= sc.biseccion_ch(Txtbox_ingreso.get())
        respuesta2,contador2= sc.regla_falsa_ch(Txtbox_ingreso.get())
        respuesta3,contador3= sc.tanteo_ch(Txtbox_ingreso.get())
        label_solucionbiseccion["text"]+="la respuesta es: " + str(respuesta) +  " \n y iteraciones:"   +str(contador) 
        label_solucionregla["text"]+="la respuesta por regla falsa es: " + str(respuesta2) + "\n y iteraciones:" + str(contador2)
        label_soluciontanteo["text"]+="la respuesta por tanteo es: " + str(respuesta3) + "\n y iteraciones:" + str(contador3)


#boton que presiona el usuario y su configuracion
Button_calcular= TK.Button(ventana,text="calcular",font= ("Arial",12),background="black",fg= "gold",command=calcular)
Button_calcular.place(x=430,y=75,anchor= "center")

#botones de chequeo
tanteo = TK.IntVar()
Checkbutton_tanteo= TK.Checkbutton(ventana,text="Tanteo",variable=tanteo,onvalue=1,offvalue=0,font= ("Arial",12),background="white",fg= "black")
Checkbutton_tanteo.place(x=180,y=115)

biseccion = TK.IntVar()
Checkbutton_biseccion= TK.Checkbutton(ventana,text="Biseccion",variable=biseccion,onvalue=1,offvalue=0,font= ("Arial",12),background="white",fg= "black")
Checkbutton_biseccion.place(x=180,y=135)

regla_falsa = TK.IntVar()
Checkbutton_reglafalsa= TK.Checkbutton(ventana,text="Regla falsa",variable=regla_falsa,onvalue=1,offvalue=0,font= ("Arial",12),background="white",fg= "black")
Checkbutton_reglafalsa.place(x=180,y=155)

#imagen
imagen1=TK.Frame(width=200,height=200)
imagen1.place(x=600,y=295)
img =TK.PhotoImage(file='materiales-clase-matematicas-cruz-lapiz-regla_318-61708.png')
imgback= TK.Label(imagen1,image=img)
imgback.pack()
Label3 = TK.Label(ventana,text=" Grafica ", font= ("Arial Black",12),background="black",fg= "gold")
Label3.place(x=615,y=255)

#soluciones
frame_Label=TK.Frame(width=200,height=200,bg='black')
frame_Label.place(x=15,y=295)
solucion=TK.StringVar
Label2 = TK.Label(frame_Label, text=" Solucion ", font= ("Arial Black",12),backgroun="black",fg= "gold")
Label2.place(x=5,y=5)
label_soluciontanteo= TK.Label(frame_Label,font= ("Arial Black",10),backgroun="black",fg= "gold")
label_soluciontanteo.pack()
label_solucionbiseccion= TK.Label(frame_Label,font= ("Arial Black",10),backgroun="black",fg= "gold")
label_solucionbiseccion.pack()
label_solucionregla= TK.Label(frame_Label,font= ("Arial Black",10),backgroun="black",fg= "gold")
label_solucionregla.pack()
#graficar
Button_graficar= TK.Button(ventana,text="graficar",font= ("Arial",12),background="black",fg= "gold")
Button_graficar.place(x=635,y=525,anchor= "center")

#grafica
#Label3= Label(ventana,x=np.linspace(-10,10,1000).astype(float)
#y=pol(X)
#plt.plot(x,0*y,'r',0*x,y,'r',x,y,'-k')
#plt.plot(X_3,pol(x_3,'ob'))
#plt.grid()
#plt.xlabel('Valores de x')
#plt.ylabel('Valores de y'))

ventana.mainloop()