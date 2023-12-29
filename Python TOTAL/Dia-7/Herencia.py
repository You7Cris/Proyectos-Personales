# Proceso mediante el cual se crea una clase hija que puede sobreescribir los metodos o atributos de una clase Padre
# Dont Repeat Yourself, para esto ayuda la herencia

class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color


    def nacer(self):
        print("Este animal ha nacido")


class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        #self.edad = edad
        #self.color = color
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("Pio")

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")

piolin = Pajaro(15, 'amarillo', 60)
mi_animal = Animal(5,'negro')

piolin.nacer()

print(Pajaro.__base__) # Me permite ver de donde hereda esta clase
print(Animal.__subclasses__())

piolin.hablar()
piolin.volar(20)

# Herencia Multiple

class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print('ja ja ja')

    def hablar(self):
        print('Que tal')

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.hablar() # Va a mostrar primero el metodo de Padre por el orden de la herencia

mi_nieto.reir() # Metodo de Madre

print(Nieto.__mro__)

# Herencia extendida
# metodos heredados, metodos modificados, atributos extras

# Herencia Multiple
# Que herede de muchas clases al mismo tiempo
