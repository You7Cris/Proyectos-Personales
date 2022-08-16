"""
EJERCICIO 3.
Escribir un porgrama que muestre los cuadrados de los 60 primeros numeros naturales.
Resolverlo con el bucle for y while.
"""

contador = 1
numero = 1

# FOR

for contador in range (61):
    print(f"{contador} * {contador} = {contador*contador}")
    contador += 1

# WHILE

while numero <= 60:
    print(f"{numero} * {numero} = {numero*numero}")
    numero += 1