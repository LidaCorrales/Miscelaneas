#Encuentre la moda de los números de la lista - Ciclos
import random
def moda_num(moda):
    for i in range (len(random1)):
            for j in range (len(random1)):
                if i !=j:
                    if random1[i]==random1[j] and random1[i] not in moda:
                        moda.append(random1[j])
    return moda

random1=[]
rango= random.randint(10,25)
moda=[]
tamaño=len(random1)
for i in range (rango):
    random1.append(round(random.random()*100))
    random1.sort()
    tamaño=len(random1)

print("Lista original", random1)
print("Numeros de moda", moda_num(moda))