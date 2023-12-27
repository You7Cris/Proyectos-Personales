mi_archivo = open('prueba.txt')

print(mi_archivo.read())

una_linea = mi_archivo.readline() # Muestra primera linea
print(una_linea)

una_linea = mi_archivo.readline() # Muestra segunda linea
print(una_linea)

una_linea = mi_archivo.readline() # Muestra tercera linea
print(una_linea.rstrip()) #Quita el salto de linea

una_linea = mi_archivo.readline() 
print(una_linea.upper()) # Se puede mostrar en mayusculas

for l in mi_archivo:
    print('Aqui dice: '+ l) # Muestra cada linea

todas = mi_archivo.readlines() # Se vuelve una lista con cada linea

todas.pop()

print(todas) 









mi_archivo.close()