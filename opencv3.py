import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#Como acceder a pixeles y modificarlos 
img=cv.imread('redbull.jpg')
img=cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)

#Accesing a pixel
px=img[100,100] #Muestra el valor del pixel seleccionado en la coordenada
print(px)

#Modify a pixel
img[100,100] = [255,0,0] #Cambia el pixel a color rojo
print(img[100,100])
