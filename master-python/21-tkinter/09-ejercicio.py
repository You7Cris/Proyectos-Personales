"""
CALCULADORA:
- 2 campos de texto
- 4 Botones para las operaciones
- Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox 
#from tkinter import messagebox as MessageBox

ventana = Tk()

ventana.geometry("400x400")
ventana.title("Calculadora")
ventana.config(bd=25)

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

def cFloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        messagebox.showerror("Error", "Introduce bien los datos")

    return result

def sumar():
    resultado.set(cFloat(numero1.get()) + cFloat(numero2.get()))
    mostrarResultado()
    

def restar():
    resultado.set(cFloat(numero1.get()) - cFloat(numero2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(cFloat(numero1.get()) * cFloat(numero2.get()))
    mostrarResultado()

def dividir():
    resultado.set(cFloat(numero1.get()) / cFloat(numero2.get()))
    mostrarResultado()

def mostrarResultado():
    messagebox.showinfo("Resultado",f" El resultado de la operacion es: {resultado.get()}")
    numero1.set("") #Borrar cuando se ejecute
    numero2.set("")


marco = Frame(ventana, width=300, height=200)
marco.config(
    padx= 15,
    pady= 15,
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False) #Para que no se deforme el marco

"""
encabezado = Label(ventana, text="Calculadora con Tkinder")
encabezado.config(
    font=("Opens Sans", 15),
)

encabezado.grid(row=0, column=0, columnspan=2, sticky=W)

# Espaciado
Label(ventana).grid(row=1, column=1)

# Texto N1
numero_1 = Label(ventana, text="Numero 1: ")
numero_1.grid(row=2, column=0, sticky=W)

# Valor N1

numero_1 = Entry(ventana, textvariable=numero1)
numero_1.grid(row=2, column=1)

# Espaciado
Label(ventana).grid(row=3, column=1)

# Texto N2
numero_2 = Label(ventana, text="Numero 2: ")
numero_2.grid(row=4, column=0, sticky=W)

# Valor N2
numero_2 = Entry(ventana, textvariable=numero2)
numero_2.grid(row=4, column=1)
"""

Label(marco, text="Numero 1: ").pack()
Entry(marco, textvariable=numero1, justify="center").pack()

Label(marco, text="Numero 2: ").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side="left", fill=X, expand=YES)



ventana.mainloop()