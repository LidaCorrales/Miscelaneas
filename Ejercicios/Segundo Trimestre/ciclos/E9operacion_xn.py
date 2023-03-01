#Calcular la operación x n sin utilizar la función pow
x = int(input("Ponga la base: "))
y = int(input("Ponga el exponente: "))
i = 1
potent = x

while(i < y):
    i+=1
    potent*=x
if y <= 0:
    potent=1
print(potent)