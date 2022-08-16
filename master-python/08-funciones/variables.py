"""
Variables locales: Se definen dentro de la funcion y no se puede usar fuera de ella, solo estan disponibles dentro.
A no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una funcion y estan disponibles dentro y fuera de ellas.

"""
# Variable global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"

print(frase)

def HolaMundo():
    frase = "Hola mundo!!"
    print("Dentro de la funcion: ")
    print(frase)

    #Variable local
    year = 2021
    print(year)

    global website
    website = "cristianweb.es"

    return "Dato devuelto " + str(year)

print(HolaMundo())
print("Fuera: ",website)
