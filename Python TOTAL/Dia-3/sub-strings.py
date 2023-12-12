# slicing

texto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fragmento = texto[2:5]
print(fragmento)

fragmento = texto[2:] #posicion 2 hasta que termine
print(fragmento)

fragmento = texto[2:10:2] #Salto de 2 en dos hasta la posicion 10
print(fragmento)

fragmento = texto[::-2]
print(fragmento)