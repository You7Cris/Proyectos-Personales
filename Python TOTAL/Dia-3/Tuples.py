mi_tuple = 1,2,3,4
mi_tuple2 = (1,2,3,4)

print(type(mi_tuple))
print(mi_tuple[2]) # 2
print(mi_tuple[-2]) #De derecha a izquierda, 3

mi_tuple = list(mi_tuple)

print(type(mi_tuple))

# Tienen que coincidir la cantidad de variables y de valores al imprimir
# x,y = t
#print(x,y,z)

t = (1,2,3,1)
print(len(t))
print(t.count(1)) # Cuantas veces aparece
print(t.index(2))