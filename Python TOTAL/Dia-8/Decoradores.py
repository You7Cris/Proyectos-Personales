
# Los decoradores añaden funcionalidad a las funciones

def mayuscula_saludo(texto):
    print('hola')
    print(texto.upper())
    print('adios')

def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())
    
    if tipo == "may":
        return mayuscula
    elif tipo == 'min':
        return minuscula


operacion = cambiar_letras('may')

operacion('palabra')

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

#@decorar_saludo
def mayusculas(texto):
    print(texto.upper())

#@decorar_saludo
def minusculas(texto):
    print(texto.lower())



#minusculas('Python')
mayuscula_decorada = decorar_saludo(mayusculas)

mayuscula_decorada('Cristian')


def una_funcion(funcion):
    return funcion

#una_funcion(mayuscula("probando"))



print('Hola')
#mayuscula('Hoy es lunes')
print()

#mi_funcion = mayuscula

#mi_funcion('python')



