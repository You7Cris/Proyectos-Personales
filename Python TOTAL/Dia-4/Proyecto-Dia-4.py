# Mi solucion
from random import *
import os

nombre = input("Cual es tu nombre?: ")
numero_adivinar = randint(1,101)
intentos = 1

print(f"Hola {nombre}, he pensado un numero entre 1 y 100, y tienes solo ocho intentos para adivinar cual crees que es el numero.")  

for n in range(1,8):
    try:
        print(f"Intento #{intentos}")
        numero = int(input("Ingresa un numero: "))
        if numero < 1 or numero > 100:
            print("Has elegido un numero que no esta permitido")
        elif numero < numero_adivinar:
            print("Respuesta incorrecta, has elegido un numero menor al numero secreto.")
        elif numero > numero_adivinar:
            print("Respuesta incorrecta, has elegido un numero mayor al numero secreto.")
        else:
            print(f"Felicitaciones, lo has logrado en #{intentos} intentos")
            break

        intentos += 1

    except ValueError:
        print("Ingresaste un dato incorrecto...")
        os.system("pause")

if numero != numero_adivinar:
    print(f"Lo lamentamos {nombre}, has perdido el juego. El numero secreto era {numero_adivinar}")

print(numero_adivinar)


# Solucion del profesor

from random import randint

estimado = 0
intentos = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")

print(f"Bueno {nombre}, he pensado un numer entre 1 y 100\n Tienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("Cuál es el numero?: "))
    intentos += 1

    if estimado not in range(1,101):
        print("Tu numero no se encuentra en el rango que va de 1 a 100")

    if estimado < numero_secreto:
        print("Mi numero es mas alto")

    elif estimado > numero_secreto:
        print("Mi numero es mas bajo")
    
    else:
        print(f"Felicitaciones {nombre}! Has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento, se han agotado los intentos. El numero secreto era {numero_secreto}")


