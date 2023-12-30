from collections import Counter
numeros = [9,4,3,2,1,5,6,7,4,7,8,9,3,4,2,1,7,5,8,7,3,4,5,3,4,5]

print(Counter(numeros)) # Muestra los elementos que se repiten

print(Counter('missisipi'))

frase = "Al pan pan y al vino vino"

print(Counter(frase.split()))

serie = Counter([1,1,1,1,1,2,3,2,2,2,2,2,3,3,3,3,3,3,4,4,4,5])
print(serie.most_common()) # Mas comun

print(list(serie))

from collections import defaultdict # diccionario por defecto

mi_dic = {'uno':'verde','dos':'azul','tres':'rojo'}
#print(mi_dic['cuatro']) # Clave que no existe

mi_dic = defaultdict(lambda: 'nada') # En caso de que no existe ese valor en el diccionario diga 'nada'

mi_dic['uno'] = 'verde'
print(mi_dic['dos'])

print(mi_dic)

from collections import namedtuple #Tupla con nombres

mi_tupla = (500, 18, 25)
print(mi_tupla[1])

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel',1.75,79)

print(ariel.altura)
print(ariel.nombre)
print(ariel[2])



