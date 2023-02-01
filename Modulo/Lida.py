def Multiplicar(num1, num2):
    Resultado = num1 * num2
    return Resultado

print(__name__)

def Suma(lista1):
    suma = 0
    for valor in lista1:
        suma = suma + valor
    return suma

def PromedioLista(lista2):
    cantidad_elementos = len(lista2)
    suma2 = 0
    for valor in lista2:
        suma2 = suma2 + valor
    promedio = suma2 / cantidad_elementos
    return promedio

def ParesImpares(Lista3):
    for num in Lista3:
        if (num % 2) == 0:  
            print("{0} es par".format(num))  
        else:  
            print("{0} es impar".format(num))

def NumeroPrimo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True