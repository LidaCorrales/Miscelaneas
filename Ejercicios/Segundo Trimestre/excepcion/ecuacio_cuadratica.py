def funcion_cua(a,b,c):
    funcion_cuadratica_suma=(-b+((b**2-(4*a*c))**0.5))//(2*a)
    funcion_cuadratica_resta = (-b-((b**2-(4*a*c))**0.5))//(2*a)
    listacuadratica = []
    listacuadratica.append(funcion_cuadratica_suma)
    listacuadratica.append(funcion_cuadratica_resta)
    return listacuadratica

while True:
    try:
        a = int(input("Ingrese el valor de a: "))
        b = int(input("Ingrese el valor de a: "))
        c = int(input("Ingrese el valor de a: "))
        if a==0 and b==0 and c==0:
            print("Programa finalizado")
            break
        print("El resultado es: ", funcion_cua(a,b,c))
    except ValueError:
        print("Los elementos son incorretos")
    except ZeroDivisionError:
        print("Division de cero errronea")
    except:
        print("Dato incorrecto")
