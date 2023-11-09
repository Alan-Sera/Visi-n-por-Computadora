import cv2
import numpy as np

img1 = cv2.imread('C:\\Users\\halo_\\Desktop\\unooooo.JPG')
img2 = cv2.imread('C:\\Users\\halo_\\Desktop\\dooooos.JPG')

a = np.array(a, dtype= float)
c = np.array(c, dtype=(np.uint8))

if img1.shape != img2.shape:
    raise ValueError("Las imágenes no tienen las mismas dimensiones")

suma = np.zeros_like(img1)
suma2 = np.zeros_like(img2)

for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        suma[i, j] = np.maximum(0, np.minimum(255, img1[i, j] + img2[i, j]))

cv2.imshow("Suma", suma)
cv2.waitKey(0)
cv2.destroyAllWindows()

