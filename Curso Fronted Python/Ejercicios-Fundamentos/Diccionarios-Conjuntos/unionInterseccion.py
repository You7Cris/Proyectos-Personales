try:
    A = [2,5,6,7,8,3,"hola","dia",73,85,34,23,"limbo"]
    B = [12,45,23,56,2,3,"mundo","lambo","limbo",46,32,67,49]
    C = []
    # Union
    A.extend(B)
    print("Union")
    print(A)

    # Interseccion
    for i in A:
        for j in B:
            if i == j:
                C.append(i)

    C = set(C)
    print("Interseccion")
    print(C)

except ValueError:
    print("Error al ingresar los datos...")