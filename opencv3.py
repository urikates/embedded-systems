import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#Como acceder a pixeles y modificarlos 
img=cv.imread('redbull.jpg')
img=cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)

#Accesing a pixel
px=img[100,100] #Muestra el valor del pixel seleccionado en la coordenada [FILA, COLUMNA]
print(px)

#Modify a pixel
img[100,100] = [255,0,0] #Cambia el pixel a color rojo
print(img[100,100])

#ROI
#Toma una cantidad de informacion o porcentaje de informacion para procesarla
roi=img[50:110, 50:110]
plt.imshow(roi)

once=img[100:250, 700:800]
plt.imshow(once)

#Para saber filas columnas y canales usar .shape
print(once.shape)

#Para mover o recolocar una cantidad de pixeles
img[100:250,1000-100:1000]=once
plt.imshow(img)

#Para modificar (cambiar el color) una region de interes
img[0:300,1000:1100]=0
plt.imshow(img)

r=img[:,:,0]
g=img[:,:,1]
b=img[:,:,2]
plt.subplot(1,4,1), plt.imshow(img), plt.title('Original')
plt.subplot(1,4,2), plt.imshow(r, 'gray'), plt.title('Red')
plt.subplot(1,4,3), plt.imshow(g, 'gray'), plt.title('Green')
plt.subplot(1,4,4), plt.imshow(b, 'gray'), plt.title('Blue')