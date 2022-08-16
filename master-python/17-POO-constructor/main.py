from coche import Coche

carro = Coche("Amarillo", "Renault", "Clio", 150, 200, 4)
carro1 = Coche("Verde", "Lamborghini", "Gallardp", 320, 600, 2)
carro2 = Coche("Rojo", "Mclaren", "Senna", 327, 675, 2)
carro3 = Coche("Gris", "Koegnisegg", "Regera", 375, 720, 2)

#print(carro.getColor())
#print(carro.getModelo())

print(carro.getInfo())
print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())


# Detectar tipado

if type(carro3) == Coche:
    print("Es un objeto correcto!!")
else:
    print("No es un objeto")


# Visibilidad

# Publicos o privados
print(carro.soy_publico)
#print(carro.__soy_privado)
print(carro.getPrivado())

