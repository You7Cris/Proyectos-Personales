# Bucles iterables (for o while)

# Loop for 
nombres = ['Juan', 'Ana', 'Carlos', 'Belen', 'Fran']

for elemento in nombres:
    numero_letra = nombres.index(elemento) + 1
    print(f"Letra {numero_letra}: {elemento}")
    print("Hola " + elemento)

lista = ['cristian','pedro', 'miguel', 'flaco', 'laura']
for nombre in lista:
    if nombre.startswith('l'): #Si el nombre empieza con l
        print(nombre)
    else:
        print(f'{nombre}: nombre que no comienza con l')

numeros = [1,2,3,4,5,6,7,8,9,10]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)

palabra = 'python es genial'

for letra in palabra:
    print(letra)

for letra in 'Cristian':
    print(letra)

for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)

dic = {'clave1':'a',
       'clave2':'b',
       'clave3':'c'}

for a,b in dic.items():
    print(a,b)


# Loops While (mienstras)
monedas = 5

while monedas < 10:
    print(f"Tengo {monedas}")
    monedas += 1
else:
    print("Ya esta a su limite de dinero")

respuesta = 's'

while respuesta == 's':
    respuesta = input("Quieres seguir? (s/n): ")
    #pass #Para que pueda continuar con lo siguiente del while
else:
    print("Gracias")

nombre = input("Tu nombre:")
for letra in nombre:
    if letra == 'r':
        break
        #break para parar el ciclo
        #continue para saltear
    print(letra)




