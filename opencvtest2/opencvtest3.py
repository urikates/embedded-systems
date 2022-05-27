import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 

#Filtros y regiones de interes

##Llama a las imagenes 
rose=cv.imread('rose.jpg')
rose=cv.cvtColor(rose, cv.COLOR_BGR2RGB)
plt.imshow(rose)

img=cv.imread('barca.jpg')
img=cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)

#Recorta la imagen
rose2=rose[800:2500,500:1300]
plt.imshow(rose2)


#Cambia el tamaño de la imagen
rose2=cv.resize(rose2,(200,400)) #Opencv maneja primero columnas y luego filas
plt.imshow(rose2)

#Seleccionamos una region de interes de barca
roi=img[0:400,0:200]
plt.imshow(roi) 

#Comenzamos el desmadre
rose2_gray=cv.cvtColor(rose2, cv.COLOR_RGB2GRAY)
#Utilizamos limites para el filtro
ret,mask=cv.threshold(rose2_gray,5, 255, cv.THRESH_BINARY) #5 muestra el limite de filtrado
plt.imshow(mask, 'gray')

mask_inv=cv.bitwise_not(mask) #Lo que es negro se vuelve blanco
plt.imshow(mask_inv, 'gray')

#Suma de las dos imagenes
image=cv.bitwise_and(rose2, rose2, mask=mask)
plt.imshow(image)

fondo=cv.bitwise_and(roi, roi, mask=mask_inv)
plt.imshow(fondo)

dest=cv.add(image,fondo)
plt.imshow(dest)

img[0:400, 0:200]=dest
plt.imshow(img)