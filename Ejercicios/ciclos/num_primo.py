num = int(input("Introduzca un numero: "))

for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
print("Es primo")