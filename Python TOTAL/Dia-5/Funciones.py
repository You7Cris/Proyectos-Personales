# def mi_funcion (parametros):
"""
Descripcion de la funcion
"""

# mi_funcion()

def saludar_persona(nombre):
    '''
    Esta funcion sirve para saludar a las personas
    '''
    print("Hola " + nombre)


saludar_persona('Cristian')
saludar_persona('Diana')

# Return

# print mostrar esa informacion al usuario
# return al devolver un resultado se puede utilizar en futuras operaciones

def multiplicar(x,y):
    total = x * y
    return total
    #return x * y

print(multiplicar(2,6))

resultado = multiplicar(7,9)
print(resultado)

