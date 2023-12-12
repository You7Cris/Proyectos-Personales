mi_lista = ['a','b','c']
mi_lista2 = ['e','f','g']
mi_lista3 = mi_lista + mi_lista2
print(type(mi_lista))

mi_lista3[0] = 'Hola'
mi_lista3.append('h') #Se agrega al final de la lista
mi_lista3.pop() #Elimina de la lista, por defecto elimina el ultimo

eliminar = mi_lista3.pop(0)

resultado = mi_lista[0:]
print(resultado)
print(mi_lista3)
print(eliminar)

lista = ['g', 'e', 'a', 'l', 'c']
lista.sort() #ordenar la lista
print(lista)

lista.reverse()
print(lista)

