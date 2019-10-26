import string
import random

claves = []

no_claves = int(input('Dame una cantidad de claves:'))
longitud = int(input('Dame la longitud: '))

mayusculas = string.ascii_uppercase
minusculas = string.ascii_lowercase
digitos = string.digits
raros = '!"·$%&/()='

contador = 1
claves_generadas = 0

while claves_generadas <= no_claves:
    cadena = ''
    numero_caracteres = 0
    while numero_caracteres <= longitud:
        if contador==1:
            cadena += random.choice(mayusculas)
            contador += 1
        elif contador==2:
            cadena += random.choice(minusculas)
            contador += 1
        elif contador==3:
            cadena += random.choice(digitos)
            contador += 1
        elif contador==4:
            cadena += random.choice(raros)
            contador = 1
        numero_caracteres += 1
    random.shuffle(list(cadena))
    claves.append(cadena)
    claves_generadas += 1

print(claves)

