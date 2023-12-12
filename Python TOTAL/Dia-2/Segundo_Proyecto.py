nombre = input("¿Cual es tu nombre?: ")
valor = int(input("Cuanto son tus ventas totales del mes?: "))
        
comision = valor * 13 / 100
print(f"La comision de {nombre} es de: ${round(comision)}")



