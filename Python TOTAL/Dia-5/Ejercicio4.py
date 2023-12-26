import os

def contar_primos(valor):
    lista = []
    total = 0

    for n in range(valor):
        if n > 1:
            contador = 0
            for i in range(2,int(n+1)):
                if n % i == 0:
                    contador += 1
                else:
                    pass
            #print(f"Contador {contador}")
            if contador == 1:
                lista.append(n)
                total += 1
    
    print(lista)
    print(f"El total de numeros primos es: {total}")
    
                

numero = 0
while numero <= 2:
    try:
        numero = int(input("Ingrese un limite para mostrar los numeros primos: "))
    except ValueError:
        print("Ingresaste un dato erroneo...")
        os.system("pause")

contar_primos(numero)

## EJERCICIO 4

def contar_primos2(numero):

    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0
    
    while iteracion <= numero:
        for n in range(3,iteracion,2):

            if iteracion % n == 0:
                iteracion += 2
                break

        else:
            primos.append(iteracion)
            iteracion += 2

    print(primos)
    return len(primos)

print(contar_primos2(150))

