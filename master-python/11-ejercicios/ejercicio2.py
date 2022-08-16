"""
Ejercicio 2.
Escribir un programa que añada valores a una lista mienstras que su longitud sea menor a 120 y luego mostrar la lista.
Plus: Usar while y for

"""

lista = []

"""
for contador in range(0, 120):
    lista.append(f"Elemento {contador+1}")
    print("Mostrando el: " + lista[contador])

print(lista)
"""
contador = 0
while contador < 120:
    lista.append(f"Elemento {contador}")
    print("Mostrando el: " + lista[contador])
    contador += 1
    