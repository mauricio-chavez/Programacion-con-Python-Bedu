"""Tablas de multiplicar"""

numero = int(input('¿Qué tabla haremos? '))

print('TABLA DE {}'.format(numero))
print('-' * 10)

for index in range(1, 11):
    print('{} x {} = {}'.format(numero, index, numero * index))

print('-' * 10)