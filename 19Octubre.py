# import cv2
# print(cv2.__version__)

import numpy as np
import cv2
img = np.zeros((600,600,3), np.uint8)
cv2.rectangle(img,(200,200),(400,400),(190,120,90),3)
cv2.imshow('Imagen', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


################################################################

import numpy as np
import cv2
img = np.zeros((600,600,3), np.uint8)
cv2.rectangle(img,(200,200),(400,400),(50,120,90),3)
cv2.circle(img,(300,300),100,(0,2550,0))
cv2.imshow('Imagen', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

################################################################

import numpy as np
import cv2
img = np.zeros((600,600,3), np.uint8)
cv2.rectangle(img,(200,200),(400,400),(50,120,90),3)
cv2.circle(img,(300,300),100,(0,2550,-1))
font = cv2.FONT.HERSHEY_SIMPLEX
cv2.putText(img,'Alan',(200,450), font, 2,(255,255,255),)
cv2.imshow('Imagen', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

################################################################
# Lectura de una Imagen

"""
 Comentarios de cadena

"""

import cv2
import numpy as np
# Cargar Imagen
A = cv2.imread('C:\\Users\\halo_\\Desktop\\buena.jpg')
# A = cv2.imread(r'C:\Users\halo_\Desktop\buena.jpg')
M,N,L = A.shape
res = cv2.resize(A,(900,800))
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.putText(res, 'Alan', (500,350), font, 2, (255,255,255))
cv2.circle(res,(600,300), 20, (100,100,0),2)
# cv2.rectangle(res,(1165,1025),(1290,1167),(50,150,50),3)
cv2.rectangle(res,(315,335),(349,381),(50,150,50),3)
cv2.imshow("Hola",res)
cv2.waitKey(0)
cv2.destroyAllWindows()


# OTRO EJERCICIO -> 

# OTRO EJERCICIO -> Crear una nueva imagen, Que gire 90° - Cambiar filas por columnas con ciclos (metodos)
