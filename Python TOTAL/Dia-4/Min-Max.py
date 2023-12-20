# min -> minimo
# max -> maximo

menor = min(58,96,72,64,35)
maximo = max(65,45,87,90,23,48)

lista = [54,23,13,78,45,72]

print(maximo)
print(max(lista))

nombres = ['Juan', 'Pablo', 'Alicia', 'Cristian']

print(min(nombres))
print(max(nombres))

nombre = "Carlos"

print(min(nombre)) # Orden de mayusculas y luego minusculas
print(min(nombre.lower()))

dic = {'C1': 45,
       'C2': 11}

print(min(dic))
print(min(dic.items()))
print(min(dic.values()))