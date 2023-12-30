import os 
import shutil

print(os.getcwd())

shutil.move('curso.txt',"C\\Users\\Cristian\\Desktop") # mover el archivo a una ruta

'''
os.unlink() # Eliminar un archivo
os.rmdir() # Eliminar directorio
shutil.rmtree() # ELiminar la carpeta junto con todo sus archivos
'''

# pip install send2trash 

# import send2trash

#send2trash.send2trash('curso.txt') # Eliminar archivo mandandolo a la papelera de reciclaje

print(os.walk('C\\Users\\Cristian\\Desktop\\Carpeta_Superior')) # walk almacena las ruta, las subcarpetas y los archivos (crea una tupla)

ruta = 'C\\Users\\Cristian\\Desktop\\Carpeta_Superior'

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta: {carpeta}')
    print(f'Las subcarpetas son: ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son: ')
    for arch in archivo:
        print(f'\t{arch}')
    print('\n')

