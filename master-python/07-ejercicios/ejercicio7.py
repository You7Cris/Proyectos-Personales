"""
EJERCICIO 7.
Hacer un programa que muestre todos los numeros impares entre dos numeros que decida el usuario.

"""
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero1 > numero2:
    for contador in range (numero2, (numero1+1)):
        if contador % 2 == 1:
            print(f"{contador}")

else:
    for contador in range (numero1,(numero2+1)):
        if contador %2 == 1:
            print(f"{contador}")
