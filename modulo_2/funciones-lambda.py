numeros = [17, 5, 7, 3, 10]

def make_square(number):
    return number **2

squares = list(map(make_square, numeros))
numeros.sort(reverse=True)
print(squares)