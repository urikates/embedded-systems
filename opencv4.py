import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

x=np.uint8([250])
y=np.uint8([10])

#numpy addition
#250+10=260; => 260/256=4
print(x+y)

#opencv addition 
#250+10=260; 255
print(cv.add(x,y))

img1=cv.imread('teamocheco.jpg')
img1=cv.cvtColor(img1, cv.COLOR_BGR2RGB)
plt.imshow(img1) 

img=np.ones(img1.shape, dtype=np.uint8)*100
plt.imshow(img, cmap='gray')

suma=cv.add(img1, img)
plt.imshow(suma)

resta=cv.subtract(img1, img)
plt.imshow(resta)

#Difumina y suma las imagenes
img2=cv.imread('redbull.jpg')
img2=cv.cvtColor(img2, cv.COLOR_BGR2RGB)
plt.imshow(img2)

#Para cambiar tamaño:
print(img1.shape)
img2=cv.resize(img2, (720,405))
plt.imshow(img2)

#destino= alpha*img+beta*img1+c
rst=cv.addWeighted(img2, 0.7, img1, 0.3, 0)
plt.imshow(rst)
#Dependiendo de la constante será la imagen que mas se vea
rst1=cv.addWeighted(img2, 0.3, img1, 0.7, 0)
plt.imshow(rst1)
