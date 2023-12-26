def ceros_vecinos(*args):

    contador = 0

    for n in args:

        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1

    return False

print(ceros_vecinos(1,0,2,5,4,3,2,1,0,2,0,2,0,0))
