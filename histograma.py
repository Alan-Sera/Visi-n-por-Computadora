import cv2
import matplotlib.pyplot as plt

# Cargar la imagen en escala de grises
imagen = cv2.imread('C:\\Users\\halo_\\Desktop\\unooooo.JPG', cv2.IMREAD_GRAYSCALE)
resG= cv2.resize(imagen,(30,20))
# Obtener las dimensiones de la imagen
filas, columnas = resG.shape

# Inicializar un array para el histograma (256 bins para escalas de grises)
histograma = [0] * 256

# Calcular el histograma
for i in range(filas):
    for j in range(columnas):
        intensidad = imagen[i, j]
        histograma[intensidad] += 1
cv2.imshow("IMagen",imagen)
# Visualizar el histograma
plt.bar(range(256), histograma, color='gray')
plt.title('Histograma de la Imagen')
plt.xlabel('Intensidad de Píxel')
plt.ylabel('Frecuencia')
plt.show()