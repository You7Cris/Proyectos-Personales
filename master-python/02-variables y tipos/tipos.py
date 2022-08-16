# Tipos de datos
#String cadena de texto, entero, booleano, etc..

nada = None #no tiene nada la variable
cadena = "Hola soy Cristian Gonzalez"
entero = 68
flotante = 4.2
booleano = True
lista = [10, 20, 30, 40, 50]
listaString = [44, "Treinta", 30, "Cuarenta"]
tuplaNoCambia = ("master", "en", "python")
diccionario = {
    "nombre" : "Cristian",
    "apellido": "Gonzalez",
    "curso" : "Master en Python"
}

rango = range(9)
dato_byte = b"Probando"

#Imprimir variable
"""print(nada)
print(cadena)
print(entero)
print(flotante)
print(booleano)
print(diccionario)
print(rango)
print(dato_byte)

# mostrar tipo de dato
print(type(nada))
print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(booleano))
print(type(diccionario))
print(type(rango))
print(type(dato_byte))"""

#Convertir datos
texto = "Hola soy un texto"
numerito = str(776)

print(texto + " " + numerito)

numerito = int(776)