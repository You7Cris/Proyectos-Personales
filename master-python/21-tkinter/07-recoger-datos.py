from cgitb import text
from tkinter import * 

ventana = Tk()
ventana.geometry("700x700")
ventana.config(
    bd=50,
    #bg="#ccc"
)

def getDato():
    resultado.set(dato.get())

    if len(resultado.get())>=1:
        texto_recogido.config(
            bg="green",
            fg="white"
        )


dato = StringVar() # Se le asigna un valor
resultado = StringVar() 

Label(ventana, text="Mete un texto: ").pack(side=LEFT, anchor=NW)
Entry(ventana, textvariable=dato ).pack(anchor=NW) #textvariable para guardar los datos

Label(ventana, text="Dato recogido: ").pack(anchor=NW)
texto_recogido = Label(ventana, textvariable=resultado)

texto_recogido.pack(anchor=NW)

Button(ventana, text="Mostrar dato", command=getDato).pack(anchor=NW)








ventana.mainloop()