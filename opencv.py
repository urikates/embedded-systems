#Utilizar codigo en spyder
import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('teamocheco.jpg') #Jalamos la imagen de la misma carpeta
plt.imshow(img) #muestra la imagen
#OPENCV utiliza BGR y MATPLOT utiliza RGB por eso se alteran los colores

#Para visualizarlo bien:
checo=cv.cvtColor(img, cv.COLOR_BGR2RGB) #Convierte la imagen BGR a RGB 
plt.imshow(checo)

print(type(checo)) #muestra el tipo de dato
print(checo.dtype) 
print(checo.shape) #Muestra el tamaño: filas, columnas, canales CADA CANAL REPRESENTA R G B
print(checo.size) #Da el numero de elementos que tiene la imagen 
print(checo.ndim) #Muestra el numero de dimensiones
print(checo.nbytes) #Da el número de Bytes
print(checo) #Da el arreglo matricial de la imagen
print(checo.max()) #Da el valor maximo
print(checo.min()) #Da el valor minimo

#Escala de grises:
img_gray=cv.cvtColor(img, cv.COLOR_RGB2GRAY)
plt.imshow(img_gray) 
print(img_gray.shape) #Al ser solo en escala de grises, ya no tiene tres canales, solo uno

plt.imshow(img_gray,cmap='gray') #Muestra la escala de grises

#Para cambiar tamaño de imagen:
#Creamos una tupla con los valores del tamaño de la imagen de checo
(filas,columnas,canales) = checo.shape
y=filas
x=columnas #Como numpy utiliza X y Y cambiamos las variables para comprenderlo mejor como columnas filas  
new_img=cv.resize(checo,(x//2,y//2)) #cambia el tamaño a la mitad 
plt.imshow(new_img)

img_flip = cv.flip(checo, -1) #voltea la imagen 
plt.imshow(img_flip)

cv.imwrite('checodecabeza.jpg', img_flip) #Guarda la imagen en la carpeta donde estas trabajando, tambien se pueden utilizar rutas 
#Sintaxis: ('Nombre_del_Archivo_nuevo.jpg',archivo a guardar)

fig=plt.figure(figsize=(10,8)) #No idea
ax=fig.add_subplot(111)
ax.imshow(img_gray, cmap='gray')


