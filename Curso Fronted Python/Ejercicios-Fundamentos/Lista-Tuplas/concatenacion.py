try:
    lista = [67,34,23,13,67,54,23,89,2,3,4,-85,-34]
    lista2 = [-10,7,34,21,67,89,-100,96,123,36]

    lista.extend(lista2)
    lista.sort()
    print(lista)

except ValueError:
    print("Error al ingresar los datos...")