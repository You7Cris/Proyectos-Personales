import os
#import shutil # Ya con esto se puede utilizar los diferentes metodos

# Crear carpeta

if not os.path.isdir("./14-sistemas-archivos/mi_carpeta"):
    os.mkdir("./14-sistemas-archivos/mi_carpeta")
else:
    print("Ya existe el directorio")


# Copiar

"""
ruta_original = "./14-sistemas-archivos/mi_carpeta"
ruta_nueva = "./14-sistemas-archivos/mi_carpeta_COPIADA"

shutil.copytree(ruta_original, ruta_nueva)
"""

# Eliminar carpeta
"""
os.rmdir("./14-sistemas-archivos/mi_carpeta_COPIADA")
"""

print("Contenido de mi carpeta: ")
contenido = os.listdir("./14-sistemas-archivos/mi_carpeta") # Listar todo lo que tenga dentro del directorio
for fichero in contenido:
    print("Fichero: "+fichero)
