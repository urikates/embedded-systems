def dado():
    import random
    return random.randint(1,6)

for i in range(10):  #for(int i=0; i<10; i++)
    d1=dado()
    d2=dado()
    suma= d1+d2
    print('Tira dado: %i'%suma)
print('Fin del ciclo for')

l=[3,4,5,5]
for i in l:
    print(i)