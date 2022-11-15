#Programa en el que se capture promedios de temperatura diaria (30 dias). LLenar aleatoriamente promedio en Soacha -
#  la mas baja unos 4 grados y el maximo 30 grados. Mostrar el promedio de temperatura de la primera mitad del mes 
# y de la segunda mitad del mes, despues de la primera tercio del mes y segundo tercio del mes.

"""import random
temp =[]
for i in range(30):
    temp.append(tam=round(random.randint(4,40)))
print("Grados:", temp)
m1 = temp[:15]
m2 = temp[15:30]
print(temp[:16])
print(temp[16:])
s1,s2 = 0, 0

for i in range(16):
    s1=s1+m1[i]
    s2 =s2+m2[i]
print("Promedio m1: ", (s1/len(m1)))
print("Promedio m2: ", (s2/len(m2)))"""

"""my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2,9]
print(my_list)
vec = []
for i in my_list:
    if i not in vec:
        vec.append(i)
print(vec)"""

#Crear una matrix donde el tamaño
# y colunmnas va a ser aleaotrio. Minimo 2 maximo 5. Lenar con numeros aleatrios e imprimir
#COMPRENSION
import random
lista=[]
lista = [round(random.random()*100) for i in range (10)]
print(lista)

impar=[x for x in lista if x%2!=0]
print(impar)
par = [x for x in lista if x&2==0]
print(par)

parimpar = ["par" if x%2==0 else "impar" for x in lista]
print(parimpar)

board = [[] for i in range(3)]
print(board)