import numpy as np

#Seleccionar el lambda a utilizar para la distribución exponencial
ld = 3
n=1000
vals = np.random.exponential(scale = 1/ld, size=n)

import pandas as pd

df = pd.DataFrame(vals)

import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(x=vals, bins=15, edgecolor = "black", color="Blue")
plt.title('Histograma de tiempos de servicio Exponencial')
plt.xlabel('Tiempos de servicio')
plt.ylabel('Frecuencia')
#plt.savefig("Hist Exponencial Original.png")
plt.show()

from scipy.stats import expon
import numpy as np
import matplotlib.pyplot as plt


x= np.arange(-0,5,0.001)
plt.plot(x, expon.pdf(x, scale = 1/5), color = "red")
plt.title(r'Función de densidad Exponencial $\lambda = 5$')
plt.xlabel('Valores')
plt.ylabel('Densidad')
#plt.savefig("Lambda3.png")
plt.show()

