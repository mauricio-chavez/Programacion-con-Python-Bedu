from pprint import pprint

user = {
    'nombre': 'Mauricio Chávez',
    'años': 20,
    'carrera': 'ciencias de la computación',
}
user['cumpleaños'] = '21 de Diciembre'
pprint(user)

cumpleaños = user.pop('cumpleaños')
pprint(user)
print(cumpleaños)
