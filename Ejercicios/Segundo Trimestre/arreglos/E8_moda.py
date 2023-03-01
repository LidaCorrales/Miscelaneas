#Encuentre la moda de los números de la lista
import random
random1=[]
rango= random.randint(10,25)
moda=[]
tamaño=len(random1)

for i in range (rango):
    random1.append(round(random.random()*100))
    random1.sort()
    tamaño=len(random1)
    for i in range (len(random1)):
        for j in range (len(random1)):
            if i !=j:
                if random1[i]==random1[j] and random1[i] not in moda:
                    moda.append(random1[j])
print(random1)
print("La moda es: ", moda)