from cgitb import text
from optparse import Option
from select import select
from tkinter import *


ventana = Tk()

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas", 20)
)
#encabezado.pack(anchor=N, side=TOP, fill=X, expand=YES)
encabezado.grid(row=0, column=0, columnspan=5, sticky=W)
# Botones check

def mostrarProfesion():
    texto = ""

    if web.get():
        texto += "Desarrollo web"

    if movil.get():
        if web.get():
            texto += "y Desarrollo movil"
        else:
            texto += "Desarrollo movil"

        

    mostrar.config(
        text=texto,
        bg="green",
        fg="white"
    )

web = IntVar()
movil = IntVar()

Label(ventana, text="¿A que te dedicas?").grid(row=1, column=0)

Checkbutton(
    ventana, 
    text="Desarrollo Web",
    variable=web,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2, column=0)

Checkbutton(
    ventana, 
    text="Desarrollo Movil",
    variable=movil,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=3, column=0)

mostrar = Label(ventana)
mostrar.grid(row=4, column=0)


# Radio buttons
def marcar():
    marcado.config(text=opcion.get())


opcion = StringVar()
opcion.set(None)

Label(ventana, text="¿Cual es tu genero?").grid(row=5)
Radiobutton(
    ventana, 
    text="Masculino",
    value="Masculino",
    variable=opcion,
    command=marcar
).grid(row=6)

Radiobutton(
    ventana, 
    text="Femenino",
    value="Femenino",
    variable=opcion,
    command=marcar
).grid(row=7)

marcado = Label(ventana)
marcado.grid(row=8)

# Option Menu

def seleccionar():
    seleccionado.config(text=opcion.get())

opcion = StringVar()
opcion.set("Opcion 1")

Label(ventana, text="Selecciona una opcion").grid(row=5, column = 1)

select = OptionMenu(ventana, opcion, "Opcion 1", "Opcion 2", "Opcion 3")
select.grid(row=6, column=1)

Button(ventana, text="Ver", command=seleccionar).grid(row=7, column=1)

seleccionado = Label(ventana)
seleccionado.grid(row=8, column=1)

ventana.mainloop()

