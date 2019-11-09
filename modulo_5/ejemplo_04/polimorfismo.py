class Perro:
    def sonido(self):
        print('Guau!')

class Carro:
    def sonido(self):
        print("Rum rum")

perro = Perro()
carro = Carro() 

lista = [perro, carro, carro, perro]

for objeto in lista:
    objeto.sonido()