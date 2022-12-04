"""def ejercicio(numero):
    if numero <= 0:
        print ("El numero es menor que cero")
    elif numero >= 0:
        print("El numero es mayor que cero")
    else:
        print("el numero es cero")
numero = int(input("Ingresar un numero"))
(ejercicio(numero))

def ejercicio2(numero2):
    if numero2 <= 3:
        print ("El numero es menor que tres")
    elif numero2 >= 3:
        print("El numero es mayor que tres")
    else:
        print("el numero es tres")

numero2 = int(input("Ingresar un numero"))
(ejercicio(numero2))

def numeroMenor10(numero):
    contador = 0
    while numero < 10:
        numero+=1
        contador+=1
        print(contador)
numero = 0
numeroMenor10(numero)

def tablasMultiplicar ():
    primero=3
    while primero<=7:
        print("tabla del "+str(primero))
        segundo=1
        while segundo<=10:
            print(str(primero)+"X"+str(segundo)+"="+ str(primero*segundo))
            segundo+=1
        primero+=1

tablasMultiplicar()

while True:
    print('1- Ejercicio condicional 1')
    print('2- Ejercicio condicional 2')
    print('3- Ejercicio bucles 1')
    print('4- Ejercicio bucles 2')
    print("5 - salir")
    ctrl=int(input('Ingrese la opcion'))
    match ctrl:
        case 1:
            print('ingreso 1')
        case 2:
            print('ingreso 2')
        case 3:
            print('ingreso 3')
        case 4:
            print('ingreso 4')
        case 5:
            print('ingreso 5')
        case _:
            print('no existe')
            break
    
    if ctrl==1:
        print('Selecciono uno')
        ejercicio()
    elif ctrl==2:
        print('Selecciono dos')
        ejercicio2()
    elif ctrl==3:
        print('Selecciono tres')
        numeroMenor10()
    elif ctrl==4:
        print('Selecciono tres')
        tablasMultiplicar()
    else:
        print('no existe la opcion')
        break"""

def llenarLista(lista,limite):
    for i in range(limite):
        lista.append(i)
    return lista

l = llenarLista([],10)
print(l)

def llenadoLista(lista,limite):
    if limite >0:
        c=0 
        while c <= limite:
            lista.append(c)
            c+=1
            return lista
    else:
        j = 0
        while j>= limite:
            lista.append(j)
            j-=1
            return lista

print(llenadoLista([], -10))