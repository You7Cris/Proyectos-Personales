from tkinter import * 

ventana = Tk()
#ventana.geometry("700x500")

texto = Label(ventana, text="Bienvenido a mi programa")

texto.config(
    fg="white", #texto en blanco
    bg="black", #Fondo en negro
    padx=50, # Relleno en el eje x
    pady=20, # Relleno en el eje y
    font=("Arial",15) #Tipo de fuente
)

texto.pack(side=TOP) # Para que cargue dentyro de la ventana

texto = Label(ventana, text="Soy Cristian Gonzalez")
texto.config(
    #justify= RIGHT,
    #width=100,
    #height=100,
    bg= "orange",
    font=("Arial", 20)
) # Estilos
texto.pack(side=TOP, fill=X, expand=YES)  #Fill X le rellena todo en X, expand habilita que se expanda la caja

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"

texto = Label(ventana, text=pruebas("Cristian","Gonzalez","Colombia"))
#texto = Label(ventana, text=pruebas(pais = "Colombia",apellidos = "Gonzalez", nombre = "Cristian"))
texto.config(
    height=3,
    bg="green",
    font=("Arial",18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(anchor=E)

texto = Label(ventana, text="Basico     ")

texto.config(
    height=3,
    bg="red",
    font=("Arial",18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Basico 2")

texto.config(
    height=3,
    bg="orange",
    font=("Arial",18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Basico")

texto.config(
    height=3,
    bg="blue",
    font=("Arial",18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()