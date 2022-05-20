#Utilizar codigo en spyder
import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

img=np.zeros((512,512,3), np.uint8)
plt.imshow(img)
#Para una imagen en blanco, utilizar unos en lugar de ceros

#Utiliza el plano X, Y para coordenadas

cv.line(img, pt1=(0,0),pt2=(512,512), color=(0,255,0), thickness=5) #crea una linea del plot1 al plot 2 
plt.imshow(img)

cv.line(img, (0,512), (512,0), (0,255,0), 5)
plt.imshow(img)

#Para crear un rectangulo
cv.rectangle(img, pt1=(100,100), pt2=(400,400), color=(0,255,255), thickness=10) #Utiliza el punto 1 y punto 2 para crear la simetria del rectangulo
plt.imshow(img)

cv.rectangle(img, (200,200), (300,300), (0,0,255), 10)
plt.imshow(img)

#Para dibujar un circulo 
cv.circle(img, center=(100,100), radius=50, color=(255,255,0), thickness=10)
plt.imshow(img)
cv.circle(img, (400,100), 50, (255,255,0), 10)
plt.imshow(img)
#Para un relleno automatico:
cv.circle(img, (400,400), 50, (255,0,0), -1) #Utilizar -1 rellena el circulo 
plt.imshow(img)
cv.circle(img, (100,400), 50, (255,0,0), -1)
plt.imshow(img)

#Guardamos imagen:
cv.imwrite('LearningOpencv.jpg', img)



