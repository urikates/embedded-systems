def dado():
    import random
    return random.randint(1,6)

def tirardados():
    import random
    d1=dado()
    d2=dado()
    suma=d1+d2
    print('Suma dados: %i' %(suma))
    return suma