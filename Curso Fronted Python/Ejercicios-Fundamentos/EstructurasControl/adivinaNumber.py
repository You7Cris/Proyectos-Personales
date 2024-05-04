import random 

try:
    number = random.randint(1,21)
    contadorIntentos = 0
    vidas = 5
    print("Adivina el numero aleatorio que esta entre el 1 y el 20")
    while vidas != 0:
        numero = int(input("Ingrese el numero: "))
        if numero == number:
            print("ACERTASTE!! Felicidades")
            break
        if numero > number:
            print("El numero es demasiado alto")
        else:
            print("El numero es demasiado bajo")
        
        vidas = vidas - 1
        print(f"Te quedan {vidas} intentos")
        print("-----------------")

    if vidas == 0:
        print("El numero era: ",number)

except ValueError:
    print("Error al ingresar el dato...")