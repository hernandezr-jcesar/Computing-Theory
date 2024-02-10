import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('CantDeUnos.txt', header=1, delim_whitespace=True)

print(data)
plt.title("Grafica de Programa1")
plt.xlabel("Cadenas")
plt.ylabel("Cantidad de Unos")
plt.grid(True)
plt.plot(data,"g")
plt.show( )
