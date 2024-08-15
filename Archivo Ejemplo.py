import numpy as np

#Seleccionar el lambda a utilizar para la distribución exponencial
ld = 3
n=1000
vals = np.random.exponential(scale = 1/ld, size=n)

import pandas as pd

df = pd.DataFrame(vals)

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(x=vals, bins=30, edgecolor = "black", color="red")
plt.title('Histograma de tiempos de servicio Exponencial')
plt.xlabel('Tiempos de servicio')
plt.ylabel('Frecuencia')
#plt.savefig("Hist Exponencial Original.png")
plt.show()