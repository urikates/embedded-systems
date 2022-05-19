import DadosFuncion
l=[0]
l2=[0]*10

for i in range(10):
    suma= DadosFuncion.tirardados()
    l.append(suma)
    l2[i]=suma

for i in l:
   print(i)

for i in l2:
    print(i)