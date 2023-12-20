palabra = 'python'

lista = [letra for letra in palabra]

print(lista)

lista = [n / 2 for n in range(0,21,2)]

print(lista)

lista = [n if n * 2 > 10 else 'no' for n in range(0,21,2) ]
print(lista)

pies = [10,20,30,40,50]

metros = [p * 3.281 for p in pies]

print(metros)

valores = [1, 2, 3, 4, 5, 6, 9.5] 

valores_pares = [p for p in valores if p%2 == 0]