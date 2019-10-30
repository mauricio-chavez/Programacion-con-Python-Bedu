import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu/')
print('El status code es ' +  response.status_code)

pikachu = response.json()
print('El peso de Pikachu es ' + pikachu['weight']