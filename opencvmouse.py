#Codigo para manejar eventos de mouse 
import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 

def draw_circle(event, x, y, flags, param):
    if event==cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),100, (255,0,0), -1)
    elif event==cv.EVENT_RBUTTONDOWN:
        cv.circle(img,(x,y),50,(0,0,255),-1)

#Creamos una imagen en negro tipo entero sin signo de 8 bits
img= np.zeros((512,512,3), np.uint8)
cv.namedWindow('imagen') #Crea una ventana para mostrar aparte la imagen 
cv.setMouseCallback('imagen', draw_circle) #Funcion que detecta evento que se hagan por el mouse en la ventana imagen, pide una funcion para pasar parametros, en este caso, dibujar circulos 
while (True): #Ciclo que muestra siempre la ventana con la imagen 
    cv.imshow('imagen', img)
    #Para poder salir del ciclo esperamos un tiempo y se debe cumplir la condicion declarada
    if cv.waitKey(5) & 0xFF==27: #presionar Tecla escape
        break
cv.destroyAllWindows()
    

