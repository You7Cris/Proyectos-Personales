# ¿ES UN NUMERO PRIMO?
i = 1

while i !=100:
    #print(i)
    contador = 0
    j = 1
    while j != i:
        if i % j == 0:
            contador = contador + 1
        else:
            pass

        j = j + 1

    if contador == 1:
        print(i)

    i = i + 1

