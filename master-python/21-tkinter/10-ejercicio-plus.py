"""
CALCULADORA:
- 2 campos de texto
- 4 Botones para las operaciones
- Mostrar el resultado en una alerta
"""

from tkinter import *
from tkinter import messagebox 
#from tkinter import messagebox as MessageBox

class Calculadora:


    def __init__(self, alertas):
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas


    def cFloat(self, numero):
        try:
            result = float(numero)
        except:
            result = 0
            messagebox.showerror("Error", "Introduce bien los datos")

        return result

    def sumar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) + self.cFloat(self.numero2.get()))
        self.mostrarResultado()
        

    def restar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) - self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def multiplicar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) * self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def dividir(self):
        self.resultado.set(self.cFloat(self.numero1.get()) / self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def mostrarResultado(self):
        self.alertas.showinfo("Resultado",f" El resultado de la operacion es: {self.resultado.get()}")
        self.numero1.set("") #Borrar cuando se ejecute
        self.numero2.set("")

ventana = Tk()

ventana.geometry("400x400")
ventana.title("Calculadora")
ventana.config(bd=25)

calculadora = Calculadora(messagebox)


marco = Frame(ventana, width=300, height=200)
marco.config(
    padx= 15,
    pady= 15,
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False) #Para que no se deforme el marco

Label(marco, text="Numero 1: ").pack()
Entry(marco, textvariable=calculadora.numero1, justify="center").pack()

Label(marco, text="Numero 2: ").pack()
Entry(marco, textvariable=calculadora.numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=calculadora.sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=calculadora.restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=calculadora.multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir", command=calculadora.dividir).pack(side="left", fill=X, expand=YES)



ventana.mainloop()