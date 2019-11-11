import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/beduExpert/B2-Programacion-con-Python/master/sesion08/ejemplo04/hoteles.csv')

df.sort_values(['rating', 'price'])
df.plot(title='Hoteles')
plt.show()