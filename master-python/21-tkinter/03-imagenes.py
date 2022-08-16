from tkinter import * 
from PIL import Image, ImageTk 


ventana = Tk()
ventana.geometry("700x500")

texto = Label(ventana, text="Soy Cristian Steven Gonzalez Arango, TU ABUELO!!")

texto.config(
    font=("Arial",18)
)

texto.pack()
# Pillow Python
# pip install --upgrade Pillow

imagen = Image.open('./21-tkinter/imagenes/Leon.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack(anchor=E)



ventana.mainloop()