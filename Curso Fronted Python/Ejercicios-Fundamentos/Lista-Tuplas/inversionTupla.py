try:
    lista = (1,5,2,8,6,3,15,12,89,67,54)
    
    for i in reversed(lista):
        print(i)

except ValueError:
    print("Error al ingresar los datos")