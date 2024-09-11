import matplotlib.pyplot as plt


x1 = [10, 20, 30]
y1 = [20, 40, 10]


x2 = [10, 20, 30]  # Nueva línea
y2 = [40, 10, 30]    # Nueva línea



plt.figure(figsize=(10, 6))

plt.plot(x1, y1, 'b-', linewidth=2, label='Línea 1')  # 'b-' significa línea azul continua

plt.plot(x2, y2, 'g-', linewidth=2, label='Línea 2')  # 'g--' significa línea verde discontinua

plt.title('Gráfico triangular con dos líneas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)


plt.xlim(10, 30)
plt.ylim(10, 40)


plt.plot(x1[0], y1[0], 'ro')  # Punto inicial Línea 1
plt.plot(x1[1], y1[1], 'ro')  # Punto medio Línea 1
plt.plot(x1[2], y1[2], 'ro')  # Punto final Línea 1


plt.plot(x2[0], y2[0], 'ms')  # Punto inicial Línea 2 (cuadrado magenta)
plt.plot(x2[1], y2[1], 'ms')  # Punto medio Línea 2
plt.plot(x2[2], y2[2], 'ms')  # Punto final Línea 2

# Agregar la leyenda
plt.legend()

# Mostrar el gráfico
plt.show()