# Tkinter es un modulo para crear interfaces graficas de usuario

from cProfile import label
from tkinter import *
import os.path 

class Programa:

    def __init__(self):
        self.title = "Master en Python"
        self.icon = "./imagenes/logo.ico"
        self.icon_alt = './21-tkinter/imagenes/logo.ico'
        self.size = "770x470"
        self.resizable = False

    def cargar(self):

        # Crear la ventana raiz

        ventana = Tk()
        self.ventana = ventana

        # Titulo de la ventana

        ventana.title(self.title)

        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        # Icono de la ventana
        #ventana.iconbitmap("./21-tkinter/imagenes/logo.ico")
        ventana.iconbitmap(ruta_icono)

        # Mostrar texto en el programa

        texto = Label(ventana, text=ruta_icono)
        texto.pack()



        # Cambio en el tamaño de la ventana

        ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)

        # Arrancar y mostrar la ventana hasta que se cierre
        #ventana.mainloop()

    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

# Instanciar mi programa

programa = Programa()

programa.cargar()
programa.addTexto("Hola soy un texto")
programa.addTexto("Bienvenido al master en Python")
programa.addTexto("Soy Cristian Gonzalez")
programa.addTexto("Ingeniero en sistemas")
programa.mostrar()




