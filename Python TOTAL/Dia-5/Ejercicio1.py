import os

'''
def devolver_distintos(lista):
    suma = 0
    mayor = 0
    menor = 0
    intermedio = 0
    contador = 0
    valor_anterior = 0
    lista.sort()
    print(lista)
    for n in lista[::-1]:
        print(n)
        if contador == 0:
            mayor = n
            menor = n
            intermedio = n
            valor_anterior = n
        else:
            pass
        
        print(f"El valor anterior es: {valor_anterior}")
        suma += n
        if contador > 0:
            if n > mayor:
                mayor = n
                
            if menor > n:
                menor = n
            
            if n > valor_anterior and n > menor:
                intermedio = n

        else:
            pass
        
        print(f"Mayor: {mayor}")
        print(f"Menor: {menor}")
        print(f"Intermedio: {intermedio}")
        contador += 1

    print(f"La suma fue {suma}")
    if suma > 15:
        print(f"El numero mayor es {mayor}")
        print(f"El numero menor es {menor}")
        print(f"El valor intermedio es {intermedio}")
    elif suma < 10:
        print(f"El numero mayor es {mayor}")
        print(f"El numero menor es {menor}")
        print(f"El valor intermedio es {intermedio}")
    else:
        print(f"El valor intermedio es {intermedio}")
        print(f"El numero mayor es {mayor}")
        print(f"El numero menor es {menor}")


lista = []
i = 4
print("Ingrese 3 numeros:")
for n in range(1,4):
    try:
        valor = int(input(f"Ingrese el #{n} numero:"))
        lista.append(valor)
    except ValueError:
        print("Vuelve a ingresar el dato correctamente....")
        os.system("pause")


devolver_distintos(lista)
'''

#### EJERCICIO 1
def devolver_distintos(a,b,c):

    suma = a + b + c
    lista = [a,b,c]

    if suma > 15:
        return max(lista)
    
    elif suma < 10:
        return min(lista)
    
    else:
        lista.sort()
        return lista[1]
    
print(devolver_distintos(20,30,5))


    
