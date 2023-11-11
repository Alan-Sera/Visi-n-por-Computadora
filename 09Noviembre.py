import cv2
import numpy as np

img1 = cv2.imread('C:\\Users\\halo_\\Desktop\\unooooo.JPG')
img2 = cv2.imread('C:\\Users\\halo_\\Desktop\\dooooos.JPG')
img3 = cv2.imread('C:\\Users\\halo_\\Desktop\\unooooo.JPG')
img4 = cv2.imread('C:\\Users\\halo_\\Desktop\\dooooos.JPG')

# a = np.array(a, dtype= float)
# c = np.array(c, dtype=(np.uint8))

if img1.shape != img2.shape:
    raise ValueError("Las imágenes no tienen las mismas dimensiones")

if img3.shape != img4.shape:
    raise ValueError("Las imágenes no tienen las mismas dimensiones")

suma = np.zeros_like(img1)

resta = np.zeros_like(img3)
resta2 = np.zeros_like(img4)

# Suma
for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        suma[i, j] = np.maximum(0, np.minimum(255, img1[i, j] + img2[i, j]))

# Resta
for i in range(img3.shape[0]):
    for j in range(img3.shape[1]):
        resta[i, j] = np.maximum(0, np.minimum(255, img3[i, j] - img4[i, j]))

# Resta2
for i in range(img3.shape[0]):
    for j in range(img3.shape[1]):
        resta2[i, j] = np.maximum(0, np.minimum(255, img4[i, j] - img3[i, j]))

# Multiplicacion punto a punto
# A[x,y,z] * B[x,y,z]
# -------------------
#       (255)

# Reflejo horizontal y vertical
############ REPORTE ###########
# Redactado en tercera persona 
# Introduccion, desarrollo y conclucion
# Lo que hicimos TODO
# Cómo hacer la transformacion
# Transpuesta
# Imagenes uint8 

# Desarrollo, diagrama de flujo de como se hace el experimento

# Conclusiones, qué aprendimos al hacer el experimento

# Referencias 
# Codigo adjunto, no en el reporte

# Cuadrado con 5 colores distintos
# Valor RGB del color

cv2.imshow("Suma", suma)
cv2.imshow("Resta", resta)
cv2.imshow("Resta2", resta2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# if (a - B) < 0 

# Practica 2 - 
# Sacar parte Roja, Verde y azul
# Imprimir parte por parte
# 
# 
# 
# 