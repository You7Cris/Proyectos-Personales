def letras_unicas(valor):
    lista = []
    contador = 0
    for n in valor:
        lista.append(n)
        print(n)

    lista2 = list(set(lista))
    lista2.sort()
    print(lista2)


valor = input("Ingresa una palabra: ")
valor = valor.lower()
print(valor)
letras_unicas(valor)

### EJERCICIO 2
def letras_unicas2(palabra):

    mi_set = set()

    for letra in palabra:
        mi_set.add(letra)
    
    mi_lista = list(mi_set)
    mi_lista.sort()
    return mi_lista

print(letras_unicas2('entretenido'))



