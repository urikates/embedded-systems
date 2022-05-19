total=0
contador=0
while contador<10:
    calif=int(input('Introduce calificación: '))
    total +=calif #total=total+calif
    contador+=1
promedio=total/10.0
print('Promedio de la clase: %.2f' %promedio)
print('Promedio de la clase: %i' %promedio)
print('Promedio de la clase: %s' %promedio)
print('Promedio: ' + str(promedio)) #El signo + hace una concatenación y el str() vuelve el valor en tipo string
#int() vuelve el dato en un tipo entero float() vuelve los archivos tipo flotante



