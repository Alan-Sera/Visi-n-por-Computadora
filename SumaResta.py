#SUMA################################################################################################

import cv2
import numpy as np

img1 = cv2.imread('C:\\Users\\halo_\\Desktop\\unooooo.JPG')
img2 = cv2.imread('C:\\Users\\halo_\\Desktop\\dooooos.JPG')

if img1.shape != img2.shape:
    raise ValueError("Las imágenes no tienen las mismas dimensiones")

suma = np.zeros_like(img1)

for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        suma[i, j] = np.maximum(0, np.minimum(255, img1[i, j] + img2[i, j]))

cv2.imshow("Suma", suma)
cv2.waitKey(0)
cv2.destroyAllWindows()

#RESTA################################################################################################

import cv2
import numpy as np

img1 = cv2.imread('C:\\Users\\halo_\\Desktop\\unooooo.JPG')
img2 = cv2.imread('C:\\Users\\halo_\\Desktop\\dooooos.JPG')

if img1.shape != img2.shape:
    raise ValueError("Las imágenes no tienen las mismas dimensiones")

resta = np.zeros_like(img1)

for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        resta[i, j] = np.maximum(0, np.minimum(255, img1[i, j] - img2[i, j]))

cv2.imshow("Resta", resta)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Aumentar brillo de imagen################################################################################################

import cv2
import numpy as np

# Cargamos la imagen 
img = cv2.imread('C:\\Users\\halo_\\Desktop\\dooooos.JPG')
img_original = cv2.imread('C:\\Users\\halo_\\Desktop\\dooooos.JPG')

# Obtenemos las dimensiones de las imagenes
height, width, channels = img.shape

# Aumentamos el brillo
for i in range(height):
  for j in range(width):
    # Obtenemos el valor de cada canal en el pixel (i,j)
    blue = img[i, j, 0]
    green = img[i, j, 1]
    red = img[i, j, 2]

    # Aumentamos el brillo de la imagen
    img[i, j, 0] = min(255, blue + 30)
    img[i, j, 1] = min(255, green + 30)
    img[i, j, 2] = min(255, red + 30)

# Mostramos la imagen resultante
cv2.imshow("Imagen Original", img_original)
cv2.imshow("Imagen Modificada", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
