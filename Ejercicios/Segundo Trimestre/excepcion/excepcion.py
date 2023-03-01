def divisores(num):
    try:        
        for i in range(num+1):
            if num%i==0:
                print(i,' es divisor')
    except ZeroDivisionError:
        print('indeterminacion')
    except TypeError:
        print(type(num),'Tipo de dato no soportado')
    except ValueError:
        print("Tipo de dato numero no soportado")

while True: 
    try:
        var = int(input("Ingrese numero: "))
        divisores(var)
        if var==0:
            break
    except ValueError:
        print("Incorrecto, ingrese valor correcto")

var=int(input('ingrese numero'))
divisores(var)
print('El programa continua en esta linea')