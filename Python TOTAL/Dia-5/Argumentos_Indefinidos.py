# *args = argumentos (numero de parametros de esa variable sean los que el usuario prefiera)
# def suma (*args): for n in args:

#def suma(a,b):
#    return a + b

def suma(*args):
    total = 0
    for n in args:
        total = total + n
    
    return total

def suma(*args):
    return sum(args)



print(suma(5,6,5,8,9,23,12,3,4))

# **kwargs = 'Key word args' - Palabras claves (Diccionarios)
# def suma(**kwargs): #algun codigo
# suma(1,2,3,4,5) o suma(a=1,b=2,c=3)

def suma(**kwargs):
    print(type(kwargs))
    suma = 0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        suma += valor
    
    return suma

print(suma(x=3,y=6,z=2))

def prueba(num1, num2, *args, **kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f'arg = {arg}')
    
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')

    
args = [100,200,300,400]
kwargs = {'x':'uno','y':'dos','z':'tres'}
prueba(15,50,*args,**kwargs)
#prueba(15,50,100,200,300,400,x='uno',y='dos',z='tres')

def describir_persona(nombre,**kwargs):
    palabra = "Características de " + nombre + ":\n"
    for clave,valor in kwargs.items():
        palabra += clave + ": " + valor + "\n"
    
    return palabra
        
print(describir_persona("María", color_ojos = "azules", color_pelo = "rubio"))
    