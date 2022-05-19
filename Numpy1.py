from re import A
import numpy as np

print('Ejercicio 1')
data = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(data)
print(data.shape)

print('Ejercicio 2')
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(b.shape)
print(b.size)
print(b.ndim)
print(b.dtype)

data = np.array([1,2,3,4,5],dtype=np.float)
print(data)
print(type(data))
np.zeros(3)
print(np.zeros(3))
print(np.zeros([2,3]))
print(np.ones(5))
print(np.diag([1,2,3]))

print(np.arange(1,4,1,dtype=np.float16))

o=np.zeros([5,5,5])
print(o.shape)

print(np.arange(1,10.1,0.3))
print(np.linspace(5,15,7))

print(np.linspace(6.3,6.3,50))

b2=np.array([5,6,7,8])

nx, ny = (3, 2)
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
xv, yv = np.meshgrid(x, y)
print(xv)
print(yv)

print(np.arange(1,10,1))
print(np.linspace(1,9,9))

m=np.random.rand(4,4)
m=np.round(m,2)
print(m)
print("///////////////")
print(m[2:,1:3])
print("///////////////")
print(m[2:,2:])
print("///////////////")
print(m[1::2,1::2])
