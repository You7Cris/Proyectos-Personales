class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    
    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'El pajaro volo {metros} metros')


Piolin = Pajaro('amarillo','canario')

Piolin.piar()
Piolin.volar(50)