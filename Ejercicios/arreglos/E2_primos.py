#Muestre cuales y cuantos son primos
import random 
random1=[]
rango= random.randint(10,25)

for i in range (rango):
    random1.append(round(random.random()*100))
print("La lista es: ", random1)
for n in random1:
    i = 1
    contador = 0
    while(n>=i):
        if n%i == 0:
            contador+=1
        i+=1
    if not contador > 2 or n <=1:
        print("El numero", n, "es primo")
