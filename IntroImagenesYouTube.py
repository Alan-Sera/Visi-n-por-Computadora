################################################################################################
#                     Imágenes Blanco y Negro
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Creamos nuestra imagen negra, de una sola matriz
#                     1 = una sola matriz, un solo canal
img = np.zeros((10,10,1), np.uint8) # Imagen 10x10x1 (tridimendional) de ceros, con un rango de 0 a 255 (uint8, 8 bits)

# Cambiamos algunos pixeles
img[0,1] = 30
img[2,3] = 50
img[4,5] = 200
img[6,7] = 140

# Mostramos los valores numéricos
print(img)

# Mostramos nuestra imagen
plt.imshow(img, cmap='gray') # Mapa de color de escala de grises
plt.show()

################################################################################################
#                     Imágenes RGB
import cv2
import numpy as np
import matplotlib.pyplot as plt
#                           3 = matrices, tres canales
img2 = 100 * np.ones((10,10,3), np.uint8) # 3 Matrices, todos los valores = 100

# Estraemos cada uno de los canales
R = img2[:,:,0]
G = img2[:,:,1]
B = img2[:,:,2]

# Modificamos el canal rojo
# R[:,:] = 0

# Modificamos los canales para obtener un amarillo
R[:,:] = 255
G[:,:] = 255
B[:,:] = 0

print(img2)

plt.imshow(img2)
plt.show()

################################################################################################
#                     Lectura de imágenes
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Lectura de imagen en escala de grises
imgray = cv2.imread('C:\\Users\\halo_\\Desktop\\imageness\\1.JPG', 0) # 1 Canal / 1 Matriz

# Opencv cambia la disposición de los canales, no es RGB, los pone en BGR
# Lectura de imagen a color RGB
imgRGB = cv2.imread('C:\\Users\\halo_\\Desktop\\imageness\\1.JPG', 1) # 3 Canales / 3 Matrices

# Lectura de imagen default
img = cv2.imread('C:\\Users\\halo_\\Desktop\\imageness\\1.JPG') # 3 Canales / 3 Matricez

# Extraemos los atributos principales de la imgray
tama = imgray.shape # Tamaño de la imagen
tipo = imgray.dtype # Tipo de dato, ejemplo: uint8
print("Tamaño Gray | Tipo de dato |", tama, tipo)

# Extraemos los atributos principales de la imgray
tamaRGB = imgRGB.shape # Tamaño de la imagen
tipoRGB = imgRGB.dtype # Tipo de dato, ejemplo: uint8
print("Tamaño Gray | Tipo de dato |", tamaRGB, tipoRGB)

# Mostramos las imágenes
cv2.imshow("Gray", imgray)
cv2.imshow("RGB", imgRGB)
cv2.imshow("IMG", img)

# Corregimos el color para la otra librería
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Mostramos la imagen corregida
plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

################################################################################################
#                     Canales RGB
import cv2
import matplotlib.pyplot as plt

# Creamos nuestra matriz principal
img = cv2.imread('C:\\Users\\halo_\\Desktop\\imageness\\1.JPG')
# Corregimos el color
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Extraemos los canales uno por uno
G = img[:,:,1]
R = img[:,:,0]
B = img[:,:,2]

print(img)

# Extraemos los canales con una funcion
# R,G,B = cv2.split(img)

# Mostramos los canales
fig = plt.figure() # Agregamos una figura completa

# Canal ROJO
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(R, cmap="gray")
ax1.set_title("CANAL ROJO")

# Canal VERDE
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(G, cmap="gray")
ax2.set_title("CANAL VERDE")

# Canal AZUL
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(B, cmap="gray")
ax3.set_title("CANAL AZUL")

# Reconstruccion
imgre = cv2.merge((R,G,B))

# Imagen ORIGINAL
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(imgre)
ax4.set_title("IMAGEN ORIGINAL")

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

################################################################################################
#                     Canales HSV
import cv2
import matplotlib.pyplot as plt

# Creamos nuestra matriz principal
img = cv2.imread('C:\\Users\\halo_\\Desktop\\imageness\\1.JPG')
# Corregimos el color a RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                   
# Corregimos el color a HSV
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Extraemos los canales con una funcion
H,S,V = cv2.split(imgHSV)
print(imgHSV)

# Mostramos los canales
fig = plt.figure() # Agregamos una figura completa

# Canal H (HUE) - MATIZ DEL COLO
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(H, cmap="gray")
ax1.set_title("CANAL H") 

# Canal S (SATURATION) - SATURACION
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(S, cmap="gray")
ax2.set_title("CANAL S")

# Canal V (VALUE) - VALOR DEL COLOR EN LA IMAGEN
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(V, cmap="gray")
ax3.set_title("CANAL V")

# Reconstruccion
imgre = cv2.merge((H,S,V))

# Imagen ORIGINAL
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(img)
ax4.set_title("IMAGEN ORIGINAL")

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

################################################################################################
#                     Guardar Imagen
import cv2
import matplotlib.pyplot as plt

# Creamos nuestra matriz principal
img = cv2.imread('C:\\Users\\halo_\\Desktop\\imageness\\1.JPG')
# Corregimos el color
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Extraemos los canales con una funcion
R,G,B = cv2.split(img)

# Mostramos los canales
fig = plt.figure() # Agregamos una figura completa

# Canal ROJO
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(R, cmap="gray")
ax1.set_title("CANAL ROJO")

# Canal VERDE
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(G, cmap="gray")
ax2.set_title("CANAL VERDE")

# Canal AZUL
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(B, cmap="gray")
ax3.set_title("CANAL AZUL")

# Reconstruccion
imgre = cv2.merge((R,G,B+100))

# Imagen ORIGINAL
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(imgre)
ax4.set_title("IMAGEN ORIGINAL")

# Guardamos la imagen
cv2.imwrite("ImagenGuardadaB.png",imgre)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
