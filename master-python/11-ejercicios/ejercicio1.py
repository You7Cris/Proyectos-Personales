"""
Ejercicio 1. Hacer una programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
- Recorrer la lista y mostrarla
- Hacer funcion que recorra lista de numeros
- Ordenarla y mostrarla
- Mostrar su longitud 
- Buscar algun elemento (que el usuario pida por teclado)

"""

from csv import excel


numeros = [9, 8, 45, 23, 34, 2, 90, 67]


#Recorrer y mostrar lista
contador = 1
for numero in numeros:
    print(f"Numero {contador}: {numero}")
    contador += 1


#Crear funcion que recorra lista y devuelva string

#forma 1
def mostrarlista():
    contador = 1
    for numero in numeros:
        print(f"Numero {contador}: {numero}")
        contador += 1

#forma 2
def mostrarlista2(lista):
    resultado = ""

    for elemento in lista:
        resultado += str(elemento)
        resultado += "\n"

    return resultado

#Ordenar y mostrar
numeros.sort()
print(f"Numeros ordenados: {numeros}")
print(mostrarlista2(numeros))

# Mostrar longitud
print(f"La lista cuenta con {len(numeros)} numeros")


# Busqueda en la lista
try:
    valor = int(input("Ingrese el numero que desea buscar: "))

    comprobar = isinstance(valor, int)
    while not comprobar or valor <= 0:
        valor = int(input("Ingrese el numero que desea buscar: "))
    else:
        print(f"Has introducido el {valor}")

    print(f"########## Busqueda en la lista numero {valor} ######## ")
    
    search = numeros.index(comprobar)
    print(f"El valor esta en la posicion: {numeros.index(valor)+1}")
except:
    print("El numero no esta en la lista")

#print(mostrarlista2(numeros))