class Pajaro:

    alas = True

    def __init__(self, color, especie): # metodo constructor, self (el mismo) - instancia del objeto que vaya a ser creado
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('azul','Tucan')

palabra = 'hola'

print(mi_pajaro.color)
print(mi_pajaro.especie)

print(f'Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}')

print(Pajaro.alas)
print(mi_pajaro.alas)

