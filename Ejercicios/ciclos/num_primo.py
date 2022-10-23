num = int(input("Introduzca un numero: "))
i = 1
c = 0

while(num > i):
    if num%i == 0:
        c+=1
    i+=1
if c > 2 or num <=1:
    print("No es primo")
else:
    print("Es primo")