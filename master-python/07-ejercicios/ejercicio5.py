"""
Ejercicio 5. Hacer un programa que muestre todos los numeros entre dos numeros que diga el usuario

"""

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero1 > numero2 :
    for contador in range (numero2,(numero1 + 1)):
        print(f"{contador}")
    else:
        print("Lista terminada")

else:
    for contador in range (numero1,(numero2 + 1)):
        print(f"{contador}")
    else:
        print("Lista terminada")