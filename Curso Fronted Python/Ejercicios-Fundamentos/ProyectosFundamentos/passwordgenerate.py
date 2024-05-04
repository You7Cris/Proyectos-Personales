"""
Generador de Contraseñas

Descripción: Crea un programa que genere contraseñas seguras basándose en criterios especificados por el usuario (longitud, inclusión de caracteres especiales, etc.).
Conceptos Clave: Listas, generación de números aleatorios, estructuras de control.

"""
import random
import string

def selectFromString(number, stringToSelect):
    selection = ''
    for _ in range(number):
        selection = selection + random.choice(stringToSelect)
    
    return selection

# print(selectFromString(5, 'abcdefg'))

def password_generator(quantitySpecialCharacters,quantityOfUppercase, quantityOfLowerCase, quantityOfNumbers):
    # specialCharacters = "#$%&'()*+,-./:;<=>?@[\]^_{|}~"
    specialChar = selectFromString(quantitySpecialCharacters, "#$%&'()*+,-./:;<=>?@[\]^_{|}~")
    upperCase = selectFromString(quantityOfUppercase, string.ascii_uppercase)
    lowerCase = selectFromString(quantityOfLowerCase, string.ascii_lowercase)
    numbers = selectFromString(quantityOfNumbers, string.digits)
    temporaryPassword = specialChar + upperCase + lowerCase + numbers
    listOfCharacters = [character for character in temporaryPassword]
    random.shuffle(listOfCharacters)
    return ''.join(listOfCharacters)
    # return ''.join(listOfCharacters)


print(password_generator(2,2,2,2))
