
try:
    print("Lista de compras")
    compras = []
    numero = 0
    while numero <= 0:
        numero = int(input("Cuantos productos quieres ingresar: "))

    for i in range(numero):
        dato = input("Ingrese el producto: ")
        compras.append(dato)

    print("Lista de productos:")
    
    for i in compras:
        print(i)
    


except ValueError:
    print("Error al ingresar los datos...")