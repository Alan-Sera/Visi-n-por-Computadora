import cv2
import numpy as np
from matplotlib import pyplot as plt

def detectar_piel(imagen):
    # Dimensiones de la imagen
    alto, ancho, _ = imagen.shape   
    # Crear una matriz para almacenar el resultado
    resultado = np.zeros_like(imagen)   
    # Iterar sobre cada píxel de la imagen
    for y in range(alto):
        for x in range(ancho):
            # Obtener los valores de los canales RGB en el píxel actual
            b, g, r = imagen[y, x] 
            # Aplicar las condiciones para la detección de piel
            if (r > 95 and g > 40 and b > 20 and
                max(r, g, b) - min(r, g, b) > 15 and
                abs(r - g) > 15 and r > g and r > b):
                # Asignar el píxel original en la imagen de resultado
                resultado[y, x] = [b, g, r]
                
    return resultado

ruta_imagen = 'C:\\Users\\halo_\\Desktop\\unooooo.JPG'  # Cambia esto por la ruta de tu imagen

# Cargar la imagen
imagen = cv2.imread('C:\\Users\\halo_\\Desktop\\unooooo.JPG')
# Llamar a la función para detectar piel
resultado_piel = detectar_piel(imagen)

# Mostrar la imagen original y el resultado
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
axs[0].set_title('Imagen original')
axs[0].axis('off')
axs[1].imshow(cv2.cvtColor(resultado_piel, cv2.COLOR_BGR2RGB))
axs[1].set_title('Resultado')
axs[1].axis('off')
plt.show()