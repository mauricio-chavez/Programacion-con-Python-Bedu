class Animal:

    def __init__(self, nombre, especie, sonido):
        self.nombre = nombre
        self.sonido = sonido
        self.especie = especie

    def grito(self):
        print("El {} hace {}".format(self.nombre, self.sonido))

    def info(self):
        print("Nombre: {} - Especie {}".format(self.nombre, self.especie))

    def __del__(self):
        print('Borrando ' + self.nombre)

    def __str__(self):
        return self.nombre + ' ' + self.especie

    def __bool__(self):
        if self.nombre == '':
            return False
        else:
            return True

gallo = Animal(nombre='gallo', sonido='quiquiriki', especie='ave')
pato = Animal(nombre='pato', sonido='quack', especie='ave')
cerdo = Animal("Cerdo", "Porcino", "Oink")

print(str(gallo))
