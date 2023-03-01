#Encuentre la desviación estandar
import random
random1=[]
rango= random.randint(10,25)
suma = 0
promedio = 0
contador = 0
desviacion = 0
tamaño2 = 0

for i in range (rango):
    random1.append(round(random.random()*100))
    suma+= random1[i]
    contador+=1
    promedio = suma // contador
    random1.sort()
    tamaño=len(random1)
    tamaño2=tamaño-1
desviacion = (suma-promedio)**2    #Calcular la distancia de media y elevarla al cuadrado
dividir = desviacion//tamaño2      #Dividir resultados
resultado_final = dividir **0.5    #Sacar la raiz cuadrada
print("La lista es: ", random1)
print("Esta es la desviacion estandar: ", resultado_final)