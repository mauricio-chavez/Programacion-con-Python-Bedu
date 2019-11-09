"""Tablas de multiplicar"""

numero = int(input('¿Qué tabla haremos? '))

cadena = 'TABLA DE {}\n'.format(numero)
cadena += '----------\n'
cadena += '{} x 1 = {}\n'.format(numero, numero * 1)
cadena += '{} x 2 = {}\n'.format(numero, numero * 2)
cadena += '{} x 3 = {}\n'.format(numero, numero * 3)
cadena += '{} x 4 = {}\n'.format(numero, numero * 4)
cadena += '{} x 5 = {}\n'.format(numero, numero * 5)
cadena += '{} x 6 = {}\n'.format(numero, numero * 6)
cadena += '{} x 7 = {}\n'.format(numero, numero * 7)
cadena += '{} x 8 = {}\n'.format(numero, numero * 8)
cadena += '{} x 9 = {}\n'.format(numero, numero * 9)
cadena += '{} x 10 = {}\n'.format(numero, numero * 10)
cadena += '----------\n'

print(cadena)