import os

ruta = os.getcwd() # obtener el directorio de trabajo actual
print(ruta)

ruta = os.chdir('D:\\xampp\\htdocs\\Proyectos-Personales\\Python TOTAL\\Dia-6')

segundaruta = 'D:\\xampp\\htdocs\\Proyectos-Personales\\Python TOTAL\\Dia-6\\prueba.txt'

elemento = os.path.dirname(segundaruta)
print(elemento)
elemento = os.path.basename(segundaruta)
print(elemento)

archivo = open('OtroDocumento.txt')

print(archivo.read())



#os.rmdir('D:\\xampp\\htdocs\\Proyectos-Personales\\Python TOTAL\\Dia-6\\otra') # remove directory - elimina la carpeta 'otra'

otro_archivo = open('D:\\xampp\\htdocs\\Proyectos-Personales\\Python TOTAL\\Dia-6\\Otrodocumento.txt')
print(otro_archivo.read())

from pathlib import Path

carpeta = Path('D:/xampp/htdocs/Proyectos-Personales/Python TOTAL/Dia-6/Otrodocumento.txt')

carpeta = Path('D:/xampp/htdocs/Proyectos-Personales/Python TOTAL/Dia-6/Otrodocumento.txt') / 'Otrodocumento.txt'

#archivo = carpeta / 'Otrodocumento.txt'

#mi_archivo = open(archivo)

#print(archivo.read())