import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

e1=np.zeros((512,512,3), np.uint8)
plt.imshow(e1)

e2=np.ones((90,90,3), np.uint8)
plt.imshow(e2)

husky=cv.imread('husky.jpg')
plt.imshow(husky)

husky=cv.cvtColor(husky, cv.COLOR_BGR2RGB)
plt.imshow(husky)

husky32=np.asarray(husky, dtype=np.uint32)
print(husky32.dtype)

husky32=cv.cvtColor(husky, cv.COLOR_RGB2GRAY)
plt.imshow(husky32)
plt.imshow(husky32,cmap='gray')

plt.imshow(husky32>127)

husky=cv.cvtColor(husky, cv.COLOR_RGB2HSV)
plt.imshow(husky)

husky2=cv.imread('husky.jpg')
husky2=cv.cvtColor(husky2, cv.COLOR_BGR2RGB)
e9=cv.cvtColor(husky2, cv.COLOR_RGB2HLS)    
plt.imshow(e9)

cv.imwrite('huskyescaladegrise.jpg',husky32)
cv.imwrite('huskyhsv.jpg', husky)
cv.imwrite('huskyhls.jpg', e9)

e11=cv.resize(husky2,(512,512))
plt.imshow(e11)

apple=cv.imread('manzana.jpg')
apple=cv.resize(apple,(512,512))
plt.imshow(apple)

plt.imshow(e11*apple)
e132=e11+apple
plt.imshow(e132)
e133=e11-apple
plt.imshow(e133)
