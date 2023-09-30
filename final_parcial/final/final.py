#librerias
import tkinter as TK
import matplotlib.pyplot as plt
import numpy as np
import seleccionador_checkbox as sc

#creacion de la ventana
ventana = TK.Tk()

#anchor de la ventana
ventana.geometry ('600x700')

#titulo de la ventana
ventana.title("Metodos Numericos")

#imagen fondo 
ventana.config(bg="gray")
imagen_fondo=TK.PhotoImage(file='Sin título-1.png')
labelimg=TK.Label(ventana,image=imagen_fondo)
labelimg.pack()

#titulo de la pagina con sus respectivas indicaciones
Label_titulo = TK.Label(ventana,text=" Soluciones de metodos numericos ", font= ("Arial Black",20),background="black",fg= "gold")
Label_titulo.place(x=300,y=15,anchor= "center")

#indicaciones al usuario y configuracion
Label_ecuacion = TK.Label(ventana,text=" ingrese la ecuacion ", font= ("Arial",12),background="black",fg= "gold")
Label_ecuacion.place(x=85,y=75,anchor= "center")

#lo que ingresa el usuario y configuracion
ecuacion= TK.StringVar()
Txtbox_ingreso= TK.Entry(ventana, background= "black", fg="white", font= ("Arial",14),textvariable=ecuacion)
Txtbox_ingreso.place(x=280,y=75,anchor= "center")

#FUNCION
def calcular ():solucion.set(sc.tanteo_ch(ecuacion))

#boton que presiona el usuario y su configuracion
Button_calcular= TK.Button(ventana,text="calcular",font= ("Arial",12),background="black",fg= "gold",command=calcular)
Button_calcular.place(x=430,y=75,anchor= "center")


#botones de chequeo
tanteo = TK.StringVar()
Checkbutton_tanteo= TK.Checkbutton(ventana,text="Tanteo",variable=tanteo,onvalue=1,offvalue=0,font= ("Arial",12),background="white",fg= "black")
Checkbutton_tanteo.place(x=80,y=115)

biseccion = TK.StringVar()
Checkbutton_biseccion= TK.Checkbutton(ventana,text="Biseccion",variable=biseccion,onvalue=1,offvalue=0,font= ("Arial",12),background="white",fg= "black")
Checkbutton_biseccion.place(x=80,y=135)

regla_falsa = TK.StringVar()
Checkbutton_reglafalsa= TK.Checkbutton(ventana,text="Regla falsa",variable=regla_falsa,onvalue=1,offvalue=0,font= ("Arial",12),background="white",fg= "black")
Checkbutton_reglafalsa.place(x=80,y=155)

#imagen
imagen1=TK.Frame(width=200,height=200)
imagen1.place(x=300,y=295)
img =TK.PhotoImage(file='materiales-clase-matematicas-cruz-lapiz-regla_318-61708.png')
imgback= TK.Label(imagen1,image=img)
imgback.pack()
Label3 = TK.Label(ventana,text=" Grafica ", font= ("Arial Black",12),background="black",fg= "gold")
Label3.place(x=315,y=255)

#soluciones
frame_Label=TK.Frame(width=200,height=200,bg='black')
frame_Label.place(x=85,y=295)
solucion=TK.StringVar
Label2 = TK.Label(frame_Label, text=" Solucion ", font= ("Arial Black",12),backgroun="black",fg= "gold",textvariable=solucion)
Label2.place(x=5,y=5)

#graficar
Button_graficar= TK.Button(ventana,text="graficar",font= ("Arial",12),background="black",fg= "gold")
Button_graficar.place(x=325,y=525,anchor= "center")

#grafica
#Label3= Label(ventana,x=np.linspace(-10,10,1000).astype(float)
#y=pol(X)
#plt.plot(x,0*y,'r',0*x,y,'r',x,y,'-k')
#plt.plot(X_3,pol(x_3,'ob'))
#plt.grid()
#plt.xlabel('Valores de x')
#plt.ylabel('Valores de y'))

ventana.mainloop()