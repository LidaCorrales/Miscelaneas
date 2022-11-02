import random 
random1=[]
rango= random.randint(10,25)
suma=0
promedio=0
cont=0
moda=[]
tamaño=len(random1)
media=0
s=0
tn=0
for i in range (rango):
    random1.append(round(random.random()*100))
    suma+=random1[i]
    cont+=1
    promedio=suma//cont
    random1.sort()
    tamaño=len(random1)
    tn=tamaño-1
    for i in range (len(random1)):
        for j in range (len(random1)):
            if i !=j:
                if random1[i]==random1[j] and random1[i] not in moda:
                    moda.append(random1[j])
    if tamaño%2 > 0:
        media=random1[tamaño//2]
s=(suma-promedio)**2
s2=s//tn
s3= s2 **0.5
print("La lista generada fue:\n",random1,"\nLa suma de los valores de la lista es=", suma,"\nEl promedio de los valores de la lista es =",promedio)
print("La moda de la lista es=", moda)
print("La mediana ed las lista es=", media)
print(s3)