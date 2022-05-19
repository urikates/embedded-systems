import numpy as np
 
print('Ejercicio 1')
data = np.array([[[1,2],[2,3]],[[3,4],[5,6]]])
print(data)
print(data.shape)
print("     ")
 
print('Ejercicio 2')
data2 = np.array([[1,2],[3,4],[5,6]])
print(data2.ndim)
print(data2.shape)
print(data2.dtype)
print("      ")
 
print('Ejercicio 3')
e3=np.arange(1,4,1, dtype=np.float16)
print(e3)
print(e3.dtype)
print("      ")
 
print('Ejercicio 4')
data3 = np.zeros([5,5,5])
print(data3)
print(data3.shape)
print("      ")
 
print('Ejercicio 5')
data4 = np.ones([5,5,5],dtype=np.int32)
print(data4)
print(data4.dtype)
print("      ")
 
print('Ejercicio 6')
print(np.arange(1,10.1,.3))
print("      ")
 
print('Ejercicio 7')
print(np.linspace(5,15,7))
print("      ")
 
print('Ejercicio 8')
print(np.linspace(6.3,6.3,50))
print("      ")
 
print('Ejercicio 9')
print('meshgrid crea una matriz coordinada con varios vectores coordinados (es decir, que sean de la misma dimension)')
nx, ny = (3, 2)
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
xv, yv = np.meshgrid(x, y)
print(xv,yv)
print("      ")
 
print('Ejercicio 10')
print(np.arange(1,10,1))
print(np.linspace(1,9,9))
print("      ")
 
print('Ejercicio 11')
m = np.random.rand(4,4)
m=np.round(m,2)
print(m)
print("      ")
 
print('Ejercicio 12')
print(m[2:,1:3])
print("-------------------------------------")
print(m[2:,2:])
print("-------------------------------------")
print(m[1::2,1::2])
print("      ")
 
print('Ejericio 13')
e13=m>0.5
print(e13)
print('Hace la operacion con cada elemento de la matriz, imprimiendo True cuando se cumple la condicion y False cuando no se cumple')
print("      ")