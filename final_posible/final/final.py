#librerias
import numpy as np
import tkinter as TK
import matplotlib.pyplot as plt
import seleccionador_checkbox as sc
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('TkAgg',force=True)
from matplotlib import pyplot as plt
from reportlab.pdfgen import canvas

#creacion de la ventana
ventana = TK.Tk()

#anchor de la ventana
ventana.geometry ('600x700')

#titulo de la ventana
ventana.title("Metodos Numericos")

#imagen fondo 
ventana.config(bg="gray")
imagen_fondo=TK.PhotoImage(file='final\Sin título-1.png')
labelimg=TK.Label(ventana,image=imagen_fondo)
labelimg.pack()

#titulo de la pagina con sus respectivas indicaciones
Label_titulo = TK.Label(ventana,text=" Soluciones de metodos numericos ", font= ("Arial Black",20),background="black",fg= "gold")
Label_titulo.place(x=300,y=15,anchor= "center")

#indicaciones al usuario y configuracion
Label_ecuacion = TK.Label(ventana,text=" ingrese la ecuacion ", font= ("Arial",12),background="black",fg= "gold")
Label_ecuacion.place(x=85,y=75,anchor= "center")
#indicaciones al usuario y configuracion
Label_derivada = TK.Label(ventana,text=" ingrese la derivada para newton raphson", font= ("Arial",12),background="black",fg= "gold")
Label_derivada.place(x=85,y=105,anchor= "center")
#lo que ingresa el usuario y configuracion
ecuacion= TK.StringVar()
Txtbox_ingreso= TK.Entry(ventana, background= "black", fg="white", font= ("Arial",14),textvariable=ecuacion)
Txtbox_ingreso.place(x=280,y=75,anchor= "center")

derivada= TK.StringVar()
Txtbox_ingreso= TK.Entry(ventana, background= "black", fg="white", font= ("Arial",14),textvariable=derivada)
Txtbox_ingreso.place(x=350,y=105,anchor= "center")

#FUNCION
def calcular ():
    respuesta = ''
    if tanteo.get() == 1:
        soluciones, b = sc.tanteo_ch(ecuacion.get(), tanteo.get())
        respuesta += '\nTanteo: ' + str(soluciones) + '\n Iteraciones: ' + str(b) + '\n'
    solucion.set(respuesta)

    if biseccion.get() == 1:
        soluciones, b1 = sc.biseccion_ch(ecuacion.get(), biseccion.get())
        respuesta += '\nBiseccion: ' + str(soluciones) + '\n Iteraciones: ' + str(b1) + '\n'
    solucion.set(respuesta)

    if regla_falsa.get() == 1:
        soluciones, c1 = sc.regla_ch(ecuacion.get(), regla_falsa.get())
        respuesta += '\nregla_falsa: ' + str(soluciones) + '\n Iteraciones: ' + str(c1) + '\n'
    solucion.set(respuesta)

    if newton.get() == 1:
        xc, b2 = sc.newton_ch(ecuacion.get(), newton.get(), derivada.get())
        respuesta += '\nnewton raphson: ' + str(xc) + '\n Iteraciones: ' + str(b2) + '\n'
    solucion.set(respuesta)

    if regla_secante.get() == 1:
        soluciones, it = sc.regla_secante(ecuacion.get(), regla_secante.get())
        respuesta += '\nregla secante: ' + str(soluciones) + '\n Iteraciones: ' + str(it) + '\n'
    solucion.set(respuesta)

    if steffensen.get() == 1:
        soluciones, b5 = sc.steffensen(ecuacion.get(), steffensen.get())
        respuesta += 'steffensen: ' + str(soluciones)+ '\n Itaraciones: ' + str(b5) + '\n'
    solucion.set(respuesta)

#grafica
def dibujo():
    imgback.place_forget()
    cuadroDibujo = TK.Frame(width=200, height=200)
    cuadroDibujo.place(x=300,y=295)
    figura, dibujo = plt.subplots(dpi=100, figsize=(2.0,2.0))
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    dibujo.axhline(linewidth=2, color='k')
    dibujo.axvline(linewidth=2, color='k')
    dibujo.set_facecolor('lightgray')
    x = np.arange(-np.pi, 4*np.pi, 0.01)
    line = dibujo.plot(x, eval(ecuacion.get()), color ='r', linestyle='solid')
    Grafica = FigureCanvasTkAgg(figura, cuadroDibujo)
    Grafica.draw()
    figura.savefig("grafica.png")
    Grafica.get_tk_widget().pack()

# Función para generar el reporte
def generar_reporte():
    # Crear el objeto Canvas
    pdf = canvas.Canvas("reporte.pdf")

    # Agregar el título
    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(100, 750, "Reporte de solución")

    # Agregar la ecuación
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 700, "Ecuación: " + ecuacion.get())

    # Agregar la solución
    pdf.drawString(100, 650, "Solución:")
    y = 630  # posición y inicial
    for line in solucion.get().splitlines():
        pdf.drawString(100, y, line)
        y -= 7  # decrementar la posición y para la siguiente línea
    # Agregar la gráfica
    pdf.drawImage("grafica.png", 100, 100, width=400, height=400)
    # Guardar el archivo PDF
    pdf.save()

#boton que presiona el usuario y su configuracion
Button_calcular= TK.Button(ventana,text="calcular",font= ("Arial",12),background="black",fg= "gold",command=calcular)
Button_calcular.place(x=430,y=75,anchor= "center")

#boton reporte
Button_generar_reporte = TK.Button(ventana, text="Generar reporte",font= ("Arial",12),background="black",fg= "gold", command= generar_reporte)
Button_generar_reporte.place(x=520,y=520,anchor="center")

#botones de chequeo
tanteo = TK.IntVar()
Checkbutton_tanteo= TK.Checkbutton(ventana,text="Tanteo",variable=tanteo,onvalue=1,offvalue=0,font= ("Arial",12),background="black",fg= "gold")
Checkbutton_tanteo.place(x=80,y=125)

biseccion = TK.IntVar()
Checkbutton_biseccion= TK.Checkbutton(ventana,text="Biseccion",variable=biseccion,onvalue=1,offvalue=0,font= ("Arial",12),background="black",fg= "gold")
Checkbutton_biseccion.place(x=80,y=145)

regla_falsa = TK.IntVar()
Checkbutton_reglafalsa= TK.Checkbutton(ventana,text="Regla falsa",variable=regla_falsa,onvalue=1,offvalue=0,font= ("Arial",12),background="black",fg= "gold")
Checkbutton_reglafalsa.place(x=80,y=165)

newton = TK.IntVar()
Checkbutton_newton= TK.Checkbutton(ventana,text="newton raphson",variable=newton,onvalue=1,offvalue=0,font= ("Arial",12),background="black",fg= "gold")
Checkbutton_newton.place(x=80,y=185)

regla_secante = TK.IntVar()
Checkbutton_regla_secante= TK.Checkbutton(ventana,text="regla secante",variable=regla_secante,onvalue=1,offvalue=0,font= ("Arial",12),background="black",fg= "gold")
Checkbutton_regla_secante.place(x=80,y=210)

steffensen = TK.IntVar()
Checkbutton_steffensen= TK.Checkbutton(ventana,text="steffensen",variable=steffensen,onvalue=1,offvalue=0,font= ("Arial",12),background="black",fg= "gold")
Checkbutton_steffensen.place(x=80,y=235)

#imagen
imagen1=TK.Frame(width=200,height=200)
imagen1.place(x=325,y=295)
img =TK.PhotoImage(file='final\materiales-clase-matematicas-cruz-lapiz-regla_318-61708.png')
imgback= TK.Label(imagen1,image=img)
imgback.pack()
Label3 = TK.Label(ventana,text=" Grafica ", font= ("Arial Black",12),background="black",fg= "gold")
Label3.place(x=315,y=255)

#soluciones
frame_Label=TK.Frame(width=300,height=325,bg='black')
frame_Label.place(x=15,y=295)

solucion=TK.StringVar()
Label2 = TK.Label(frame_Label, font= ("Arial",10),backgroun="black",fg= "gold", textvariable=solucion)
Label2.place(x=5,y=5)

#graficar
Button_graficar= TK.Button(ventana,text="graficar",font= ("Arial",12),background="black",fg= "gold", command=dibujo)
Button_graficar.place(x=355,y=525,anchor= "center")

#frame
cuadroDibujo = TK.Frame(width=280, height=200)

ventana.mainloop()