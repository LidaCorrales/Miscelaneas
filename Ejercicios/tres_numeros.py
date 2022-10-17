print("COMPARADOR DE TRES NÚMEROS")
numero1 = float(input("Escriba un número: "))
numero2 = float(input("Escriba otro número: "))
numero3 = float(input("Escriba otro número más: "))

if numero1 == numero2 == numero3:        
    print("Ha escrito tres veces el mismo número.")
elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:        
    print("Ha escrito uno de los números dos veces.")
else:        
    print("Los tres números que ha escrito son distintos.")