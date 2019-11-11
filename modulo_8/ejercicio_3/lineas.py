import numpy as np
import matplotlib.pyplot as plt

# Los ejes pueden ser tuplas, listas, o arrays de numpy
x = (4,8,13,17,20)
y = (54, 67, 98, 78, 45)

plt.plot(np.array(x), np.array(y))
plt.show()  # Muestra en pantalla la gráfica interactiva