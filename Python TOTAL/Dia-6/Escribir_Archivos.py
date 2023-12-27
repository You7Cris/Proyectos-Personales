#archivo = open('prueba.txt', 'r') # Solo lectura aunque por defecto python lo toma asi

archivo = open('prueba.txt', 'w') # Sobreescribe si ya existe el contenido

#archivo = open('prueba.txt', 'a') # Agregar al archivo
archivo.write('Soy el nuevo texto')
archivo.write('Hola\n')
archivo.write('Mundo')


archivo.writelines(['hola','mundo','aqui','estoy']) #Agregar muchas lineas, se puede realizar con listas

listas = ['hola','mundo','aqui','estoy']
for p in listas:
    archivo.writelines(p + '\n')


archivo.close()