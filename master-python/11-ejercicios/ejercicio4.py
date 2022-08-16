"""
Ejercicio 4. 
Crear un script que tenga 4 variables, 1 lista, 1 string, 1 entero y un booleano y que imprima un mensaje segun el tipo de dato de cada variable. Usar funciones 
"""

from cgitb import text


def comprobar_tipado(variable, tipo):
    test = isinstance(variable, tipo)
    result = ""

    if test:
        result = f"Este dato es del tipo {type(variable)}"
    else: 
        result = "El tipo de dato no es correcto"
    
    return result



mi_lista = ["Hola mundo", 44, "Cristian"]
texto = "Master en Python"
entero = 67
booleano = True

print(comprobar_tipado(mi_lista, list))
print(comprobar_tipado(texto, str))
print(comprobar_tipado(entero, int))
print(comprobar_tipado(booleano, bool))


    


