#Zip combinar 2 o mas listas en Tuples

nombres = ["Cristian","Hugo","Valeria"]
edades = [24,32,45]
ciudades = ["Lima","Madrid","Cartago","Maracaibo","Paris"]

combinados = list(zip(nombres,edades,ciudades))

print(combinados)

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
