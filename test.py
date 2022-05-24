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

# img=np.ones(img1.shape, dtype=np.uint8)*100
# plt.imshow(img, cmap='gray')

# suma=cv.add(img1, img)
# plt.imshow(suma)

# resta=cv.substract(img1, img)
# plt.imshow(resta)