def saludar(*nombres):
    for nombre in nombres:
        print('Hola, ' + nombre)

def sumar(*args):
    return sum(args)

def funcion(*args, **kwargs):
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg)

def user_info(**kwargs):
    for key, value in kwargs.items():
        print('El ' + key + ' es ' + str(value))

def dividir(dividendo, divisor):
    print(dividendo / divisor)

dividir(divisor=2, dividendo=3)