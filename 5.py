import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 5, 21)  

plt.figure()

plt.plot(x, x-x, 'g--', label='y = linea')          # Línea verde discontinua
plt.plot(x, x**2, 'bs', label='y = cuadrado ')       # Cuadrados azules
plt.plot(x, x**3, 'r^', label='y = triangulo')       # Triángulos rojos

plt.title('Gráficos')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

plt.xlim(0, 5)  
plt.ylim(0, 120)  


plt.show()
