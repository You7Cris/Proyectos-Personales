
'''
def chequear_3_cifras(numero):
    return numero in range(100,1000)

'''


def chequear_3_cifras(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass

    return lista_3_cifras


resultado = chequear_3_cifras([55,89,5000,30000,765,127])
print(resultado)
print(type(resultado))