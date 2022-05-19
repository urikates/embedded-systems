s1='Nombre: %s, Edad: %i, Matricula: %i' %('Jose',20,2008)
print(s1)
print('Temperatura: %f, Humedad: %.2f' %(30.2,12.0034)) #Solo trabaja con Tuplas
#print("T: %f, Humedad: %0.3f" %[20.04,90.003]) -> Esto no funciona debido a que es una lista y esto utiliza tuplas
print('Comandos de Linux: {},{},{} y {}'.format('cd','ls','cp','pwd')) #Debe tener la misma cantidad de corchetes y la misma cantidad de datos a ingresar
print('T: {}, H: {}'.format(0.3324,12.36548)) #.format(), vuelve el valor en un string y lo introduce en corchetes conforme el orden

c="Pyhton3,Python,RaspberryPy"
print(c.find('Py')) #Entrega el índice (número) de la palabra que estamos buscando
indice=c.find('Py',6)
print(indice)
print(c.find('Py',12))

l1=['20.03','40.02','90']
l2=[20.03,40.02,90]
s='*'
print(s.join(l1))
# print(s.join(l2)) ->Solo se puede utilizar con cadenas de texto
s1='/*'
print(s1.join(l1))

