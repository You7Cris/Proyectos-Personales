from importlib.resources import path
from io import open
import pathlib
import shutil # Se puede acceder a diferentes funciones para copiar, renombrar, eliminar archivos

#Abrir un archivo

ruta = str(pathlib.Path().absolute()) + "./14-sistemas-archivos/fichero_texto.txt"
archivo = open(ruta, "a+")

# Escribir

archivo.write("*******Soy un texto metido desde python**********\n")

# Cerrar archivo
archivo.close()

#Abrir un archivo

ruta = str(pathlib.Path().absolute()) + "./14-sistemas-archivos/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# Leer contenido 

#contenido = archivo_lectura.read()
#print(contenido)

# Leer contenido y guardarlo en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

#print(lista)

for frase in lista:
    #if not frase.isnumeric():
    lista_frase = frase.split() #Sirve para que una frase se convierta en una lista
    #print(lista_frase)
    #print("- "+frase.upper())
    print("- "+frase.center(100))

# Copiar
"""
ruta_original = str(pathlib.Path().absolute()) + "./14-sistemas-archivos/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/../14-sistemas-archivos/fichero_copiado.txt"
#ruta_alternativa = str(pathlib.Path().absolute()) + "./13-paquetes/fichero_copiado1.txt"
shutil.copyfile(ruta_original, ruta_nueva)
"""


# Mover 
"""
ruta_original = str(pathlib.Path().absolute()) + "./14-sistemas-archivos/fichero_copiado.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "./14-sistemas-archivos/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original, ruta_nueva)
"""

# Eliminar 
import os

"""
ruta_nueva = str(pathlib.Path().absolute()) + "./14-sistemas-archivos/fichero_copiado_NUEVO.txt"
os.remove(ruta_nueva)
"""

# Comprobar si existe
import os.path

#print(os.path.abspath("../"))
#ruta_comprobar = os.path.abspath("./") + "fichero_texto55.txt"
#print(ruta_comprobar)
ruta_comprobar = "./ficheros.py"

if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")

