import random

tam=int(input("Cuantos numeros: "))
vector=[]
par= 0
impar=0
total=0
total2=0
promedio1=0
promedio2=0
for i in range(tam):
    vector.append(round(random.random()*100))
print(vector)

for i in range(tam):
    #print("posicion", i, "elemento", vector[i])
    if vector[i]%2==0:
        print(vector[i], "es par")
        par+=1 
        total+=vector[i]
        promedio= total//par
    else:
        print(vector[i], "es impar")
        impar+=1
        total2+=vector[i]
        promedio2=total2//impar
print("Pares son: ", par, "Impares cantidades: ", impar)
print("Suma pares", total, "Suma Impares: ", total2)    
print("Promedio pares", promedio1, "Promedio impares", promedio2)