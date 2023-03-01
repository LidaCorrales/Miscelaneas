#Diseñar e implementar un programa que solicite a su usuario un valor no negativo n y visualice la siguiente salida:
#1 2 3 ........ n-1 n
#1 2 3 ........ n-1
#.........
#1 2 3
#1 2
#1
num = int(input("Ingresar valor positivo: "))

while num > 0:
    num2=""
    for i in range (0,num+1):
        num2+=str(i)
    print(num2)
    num-=1