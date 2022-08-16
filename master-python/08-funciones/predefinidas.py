nombre = "Cristian Gonzalez"

#Funciones generales
print(nombre)
print(type(nombre))

# Detectar el tipado
comprobar = isinstance(nombre, str)

if comprobar:
    print("Esa variable es un string")
else:
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un numero con decimales")

# Limpiar espacios

frase = "    mi contenido      "
print(frase.strip())


# Eliminar variables

year = 2022
print(year)

del year 
#print(year)

# Comprobar variable vacia
texto = " ff "

if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print("La variable tiene contenido: ",len(texto))

# Encontrar caracteres 

frase = "La vida es bella"
print(frase.find("vida"))

frase.isalpha()

# Reemplazar palabras en un string

nueva_frase = frase.replace("vida","moto")
print(nueva_frase)

# Mayusculas y minusculas
print(nombre)
print(nombre.lower()) # Minuscula
print(nombre.upper()) # Mayuscula