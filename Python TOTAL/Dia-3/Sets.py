set([1,2,3,4,5,6]) # En un set los elementos no se repiten, solo deja los valores unico

{1,2,3,4,5,6}

mi_set = set((1,2,3,4,5))
mi_set = set((1,2,3,4,(1,2,3),1,1,1,1,1,8,5))
print(type(mi_set))
print(mi_set)  

print(len(mi_set))
print(2 in mi_set)

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

s1.add(7)
print(s1)

#s1.remove(6) #Si no existe da error
s1.discard(6) #Si no existe no pasa nada

s1.pop()

s1.clear()
print(s1)