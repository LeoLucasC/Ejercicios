import matplotlib.pyplot as plt
import numpy as np

# Crear datos para el gráfico
x = np.linspace(0, 10, 100)
y = 2 * x + 1  

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'r-')  


plt.title('Gráfico de una línea diagonal')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)


plt.show()