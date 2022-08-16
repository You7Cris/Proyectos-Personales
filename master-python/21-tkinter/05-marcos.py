from argparse import _VersionAction
from cmath import exp
from multiprocessing.connection import answer_challenge
from tkinter import *

ventana = Tk()

ventana.title("Marcos | Master en Python")
ventana.geometry("700x700")

marco_padre = Frame(ventana, width=250, height=250)
"""
marco_padre.config(
    bg="lightblue",
    #bd = 5,    # Tamaño del borde
    relief=SOLID # borde solido
)
"""
marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES) #anchor = Anclaje

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="green",
    bd = 5,    # Tamaño del borde
    relief=SOLID # borde solido
)
marco.pack(side=LEFT, anchor=SW) #anchor = Anclaje

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="red",
    bd = 5,    # Tamaño del borde
    relief=SOLID # borde solido
)
marco.pack(side=RIGHT, anchor=SE) #anchor = Anclaje

marco.pack_propagate(False) # Evitar que se contraiga el marco y conserve su tamaño original
#Label(marco, text="Primer marco").pack(side=LEFT,anchor=CENTER)
texto = Label(marco, text="Primer marco")
texto.config(
    bg="red",
    fg="white", #Color de la letra
    font=("Arial",20),
    #height=10,
    #width=10,
    #bd=3,
    #relief=SOLID
    
)
texto.pack(anchor=CENTER, fill=Y, expand=YES)

marco_padre = Frame(ventana, width=250, height=250)
"""
marco_padre.config(
    bg="lightblue",
    #bd = 5,    # Tamaño del borde
    relief=SOLID # borde solido
)
"""

marco_padre.pack(side=TOP, anchor=N,  fill=X, expand=YES) #anchor = Anclaje

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="blue",
    bd = 5,    # Tamaño del borde
    relief=SOLID # borde solido
)
marco.pack(side=LEFT) #anchor = Anclaje

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg="orange",
    bd = 5,    # Tamaño del borde
    relief=SOLID # borde solido
)
marco.pack(side=RIGHT) #anchor = Anclaje

ventana.mainloop()