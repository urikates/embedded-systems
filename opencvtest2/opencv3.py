import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt 
#Imagenes a trabajar
barca=cv.imread('barca.jpg')
barca=cv.cvtColor(barca, cv.COLOR_BGR2RGB)
plt.imshow(barca)

apple1=cv.imread('img.png')
apple1=cv.cvtColor(apple1, cv.COLOR_BGR2RGB)
plt.imshow(apple1)

apple2=cv.imread('img.png')
apple2=cv.cvtColor(apple2, cv.COLOR_BGR2RGB)
plt.imshow(apple2)

rose=cv.imread('rose.jpg')
rose=cv.cvtColor(rose, cv.COLOR_BGR2RGB)
plt.imshow(rose)

#Modificacion de imagen, recorte y tamaño
rose2=rose[800:2500,500:1300]
plt.imshow(rose2)

rose2=cv.resize(rose2,(200,400))
plt.imshow(rose2)

#Trabajo para colocar rose2
#Region de interes para rose2
roi=barca[0:400,0:200]
rose2_gray=cv.cvtColor(rose2, cv.COLOR_RGB2GRAY)
ret, mask=cv.threshold(rose2_gray, 5, 255, cv.THRESH_BINARY)
mask_inv=cv.bitwise_not(mask)

#Suma de las imagenes
roseimage=cv.bitwise_and (rose2, rose2, mask=mask)
fondorose=cv.bitwise_and(roi, roi, mask=mask_inv)
destrose=cv.add(roseimage,fondorose)
barca[0:400, 0:200]=destrose 
plt.imshow(barca)

#Trabajo para colocar apple1
roi2=barca[500:700,0:200]
plt.imshow(roi2)
apple1_gray=cv.cvtColor(apple1, cv.COLOR_RGB2GRAY)
ret, maskapple1=cv.threshold(apple1_gray, 5, 255, cv.THRESH_BINARY)
mask_invapple1=cv.bitwise_not(maskapple1)

#Suma de las imagenes
apple1image=cv.bitwise_and(apple1,apple1, maskapple1)
fondoapple1=cv.bitwise_and(roi2, roi2, mask=mask_invapple1)
destapple1=cv.add(apple1image, fondoapple1)
barca[500:700,0:200]=destapple1
##plt.imshow(barca)

#Trabajo para colocar apple2
roi3=barca[500:700,700:900]
#plt.imshow(roi3)
fondoapple2=cv.bitwise_and(roi3, roi3, mask=mask_invapple1)
destapple2=cv.add(apple1image, fondoapple2)
barca[500:700,700:900]=destapple2
plt.imshow(barca)