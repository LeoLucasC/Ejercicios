import matplotlib.pyplot as plt

x1 = [1, 4, 5,6,7]
y1 = [2, 6, 3,6,3]

plt.figure(figsize=(10, 6))

plt.plot(x1, y1, 'b--', linewidth=2, label='Línea 1') 


plt.title('Gráfico triangular con dos líneas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.grid(True)

plt.xlim(1,8)
plt.ylim(1,8)

# Marcar los puntos específicos de la primera línea
plt.plot(x1[0], y1[0], 'ro')  
plt.plot(x1[1], y1[1], 'ro')
plt.plot(x1[2], y1[2], 'ro')  
plt.plot(x1[3], y1[3], 'ro')  
plt.plot(x1[4], y1[4], 'ro')  


plt.legend()


plt.show()