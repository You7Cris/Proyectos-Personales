import os

while True:
    try:
        print("Generador de nombre de usuario")
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        anio = int(input("Ingresa tu año de nacimiento: "))
        nombreUser = nombre + apellido + str(anio)
        print("Su nombre de usuario sera " + nombreUser)
        exit()

    except ValueError:
        print("Datos incorrectos...")
