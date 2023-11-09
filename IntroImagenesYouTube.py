import cv2
import numpy as np
import matplotlib.pyplot as plt

# Creaamos nuestra imagen negra
img = np.zeros((10,10,1), np.uint8)

# Cambiamos algunos pixeles
img[0,1] = 30
img[2,3] = 50
img[4,5] = 200
img[6,7] = 140

# Mostramos los valores numéricos
print(img)

# Mostramos nuestra imagen
plt.imshow(img, cmap='gray')
plt.show()
