"""
Ejercicio 2. Escribir un script que nos muestre por pantalla todos los numeros pares del 1 al 20

"""

numero = 1
contador = 1

for contador in range(1, 121):
    if contador % 2 == 0:
        print(f"Numero {contador}")

    contador += 1


while numero <= 120:
    if numero % 2 == 0:
        print(f"Numero {numero}")

    numero += 1


    