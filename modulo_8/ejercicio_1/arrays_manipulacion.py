import numpy as np

# coeficientes = np.array([
#     [2, 1, -3],
#     [5, -4, 1],
#     [1, -1, -4],
# ])

# resultados = np.array([7, -19, 4])

# solucion = np.linalg.solve(coeficientes, resultados)

# print(solucion)

# print(np.allclose(np.dot(coeficientes, solucion), resultados))

a = np.array([1, 2, 3, 4])
np.savetxt('test1.txt', a, fmt='%d')
b = np.loadtxt('test1.txt', dtype=int)
print(a == b)

np.save("test.npy", a)
b = np.load("test.npy")
print(a == b)