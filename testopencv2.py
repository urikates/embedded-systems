import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt 

img=np.zeros((512,512,3), np.uint8)
plt.imshow(img)

cv.rectangle(img, (100,100), (400,400), (0,255,0), 10)
plt.imshow(img)

cv.line(img, pt1=(0,0), pt2=(100,100), color=(255,255,0), thickness=10)
plt.imshow(img)

cv.line(img, (0,512), (100,400), (255,255,0), 10)
plt.imshow(img)

cv.line(img, (512,0), (400,100), (255,255,0), 10)
plt.imshow(img)

cv.line(img, (512,512), (400,400), (255,255,0), 10)
plt.imshow(img)

cv.rectangle(img, (200,200), (300,300), (0,0,255), -1)
plt.imshow(img)

cv.circle(img, center=(100,100), radius=50, color=(255,0,255), thickness=10)
plt.imshow(img)

cv.circle(img, (400,400), 50, (255,0,255), 10)
plt.imshow(img)

font=cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, text='Uriel', org=(100,400), fontFace=font, fontScale=3.5, color=(255,255,255), thickness=3, lineType=cv.LINE_AA)
plt.imshow(img)

cv.imwrite('opencvtest2.jpg', img)