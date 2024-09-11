import matplotlib.pyplot as plt


x = [1, 2, 3]
y = [2, 4, 1]  


plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2)  # 'b-' significa línea azul continua


plt.title('Gráfico triangular abierto')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)


plt.xlim(1.0, 3.0)
plt.ylim(1.0, 4.0)


plt.plot(x[0], y[0], 'ro')  # Punto inicial
plt.plot(x[1], y[1], 'ro')  # Punto medio (punta)
plt.plot(x[2], y[2], 'ro')  # Punto final



plt.show()