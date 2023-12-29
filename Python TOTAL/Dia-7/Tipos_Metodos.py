class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    
    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pajaro volo {metros} metros')
        self.piar()

    def pintar_negro(self): # Metodos de instancia - Pueden modificar el valor de los atributos, pueden acceder a otros metodos y modificar el estado de la clase 
        self.color = 'negro'
        print(f'Ahora el pajaro es {self.color}')

    # Metodo de clase
    @classmethod

    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
       # print(f"Es de color {self.color} ") # No recibe como argumento self sino clase)
        cls.alas = False
        print(Pajaro.alas)

    # Metodo estatico - Nose refieren ni a la clase ni a la instancia, no pueden modificar ninguna instancia, no se pueden relacionar con las instancias ni modificar los atributos de la clase
    def mirar():
        print("El Pajaro mira")


# Pajaro.poner_huevos(3)
Pajaro.mirar()

'''Piolin = Pajaro('amarillo','canario')

Piolin.piar()
Piolin.volar(50)
Piolin.pintar_negro()
Piolin.alas = False
print(Piolin.alas)
'''

