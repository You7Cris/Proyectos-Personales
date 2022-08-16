"""
LISTAS(arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico nombre.

Para acceder a esos valores podemos usar un indice numerico.

"""

pelicula = "Batman"

# Definir una lista 
peliculas = ["Batman","Spiderman","El señor de los anillos"]
cantantes = list(('2pac','Drake','Jennifer Lopez'))
years = list(range(2020, 2050))
variada = ["Victor",30,4.4,True, "Texto"]

"""
print(peliculas)
print(cantantes)
print(variada)
"""

# Indices
print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[2:])

#Añadir elementos a lista
cantantes.append("Kase 0")
print(cantantes)

#cantantes.append(input("Ingrese el nuevo cantante: "))

print(cantantes)

"""
#Recorrer una lista
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n*********LISTADO DE PELICULAS********")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}.{pelicula}")
"""

# Listas multidimensionales
print("\n**********Listado de contactos*********")
contactos = [
    [
        'Antonio',
        'antonio@antonio.com'
    ],
    [
        'Cristian',
        'cristian@gmail.com'
    ],
    [ 
        'Adrian',
        'adrian@gmail.com'
    ]
]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")

#print(contactos[1][1])



