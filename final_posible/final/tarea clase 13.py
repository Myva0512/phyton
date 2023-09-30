import numpy as np

# Datos de ejemplo
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])

# Calcular las medias de x e y
media_x = np.mean(x)
media_y = np.mean(y)

# Calcular la pendiente de la recta de regresión
pendiente = np.sum((x - media_x) * (y - media_y)) / np.sum((x - media_x)**2)

# Calcular la intersección en el eje Y de la recta de regresión
interseccion = media_y - pendiente * media_x

# Imprimir la pendiente y la intersección en la consola
print("La pendiente de la recta de regresión es:", pendiente)
print("La intersección en el eje Y de la recta de regresión es:", interseccion)
