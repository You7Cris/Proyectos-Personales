# ¿ ES UN ANAGRAMA?

def palabra(palabra):
    if palabra.isalpha():
        return True
    else:
        print("Tiene caracteres que no estan en el vocabulario")
        return exit()

def anagrama(palabra1, palabra2):

    if palabra1 == palabra2:
        return False
    else:
        palabra1 = list(palabra1)
        ordenar1 = sorted(palabra1)
        print(ordenar1)
        palabra2 = list(palabra2)
        ordenar2 = sorted(palabra2)
        print(ordenar2)
        if ordenar1 == ordenar2:
            respuesta = True
            return print(f"{respuesta}")
        else:
            respuesta = False
            return print(f"{respuesta}")
        

try:
    palabra1 = input("Ingrese la palabra 1: ")
    palabra(palabra1)
    palabra2 = input("Ingrese la palabra 2: ")
    palabra(palabra2)

    anagrama(palabra1, palabra2)
except ValueError:
    print("Ocurrio un error al ingresar la palabra")

