from tkinter import *
from tkinter import messagebox as MessageBox # Modulo de alertas

ventana = Tk()

ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showinfo("Alerta", "Soy Cristian Gonzalez")
    # showerror


Button(ventana, text="Mostrar alerta!!!", command=sacarAlerta).pack()

def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "Continuar ejecutando la aplicacion? ")
    if resultado != "yes":
        MessageBox.showinfo("Hasta la proxima!!", f"Adios {nombre}")
        ventana.destroy()
    
Button(ventana, text="Salir", command=lambda: salir("Cristian")).pack()

ventana.mainloop()