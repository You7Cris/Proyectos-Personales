# enumerate acceder a los indices.

lista = ['a','b','c']
indice = 0

for item in lista:
    print(indice,item)
    indice += 1

for item in enumerate(lista):
    print(item)

for indice in enumerate(range(50,55)):
    print(indice)

mis_tuples = list(enumerate(lista))
print(mis_tuples)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    print(f"{nombre} se encuentra en el indice {indice}")