diccionario = {
    'c1':'valor1',
    'c2':'valor2'
}

print(type(diccionario))
print(diccionario)

resultado = diccionario['c1']
print(resultado)

cliente = {'nombre': 'Cristian',
    'apellido':'Gonzalez',
    'peso': 72,
    'talla': 1.75           
}

consulta = (cliente['apellido'])
print(consulta)

dic = {
    'c1':55,
    'c2': [10,20,30],
    'c3': {'s1':100, 's2':200}
}

print(dic['c3']['s2'])

dic = {
    'c1': ['a','b','c'], 
    'c2': ['d','e','f']
}

print(dic['c2'])
print(dic['c2'][1])
print(dic['c2'][1].upper())

dic = {
    1 : 'a',
    2 : 'b'
}
print(dic)

dic[3] = 'c'
print(dic)

dic[2] = 'B'
print(dic)

print(dic.keys()) #claves
print(dic.values()) #valores del diccionario
print(dic.items()) #muestra todo

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}

mi_dic["nombre"] = "Cristian"
mi_dic["apellido"] = "Gonzalez"
mi_dic["edad"] = 24
mi_dic["ocupacion"] = "Desarrollador"
mi_dic["pais"] = "Colombia"

print(mi_dic)