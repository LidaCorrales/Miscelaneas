'''import random
#intervalo=int(random.randint(-100,100))
x=int(random.randint(-100,100))'''
"""y=int(random.randint(-100,100))
if x<0:
    x*=1
    print("x es negativo")
elif y<0:
    y*=-1
    print("y es negativo")
print('x= ',x)
print('y= ',y)
if x<y:
    x,y=y,x
if x%y==0:
    print(x,'es multiplo de ',y)
else:
    print(x,'No es multiplo de ',y)"""

"""def progresionNumerica():q
    num1=-1
    num2=0
    cont=0
    while num1<num2:
        num1=num2
        num2=int(input('ingrese numero')) 

        cont+=1     
    print('Cantidad de numeros ingresada ',cont)

progresionNumerica()"""

"""def fatoresPrimos (numero):
    div=2
    while div<=numero:    
        if numero%div==0:
            print(div)
            numero/=div
        else:
            div+=1

numero =int(input("Ingrese: "))
fatoresPrimos(numero)"""

import random
num= 0

numero=int(random.randint(50, 100))
for i in range (numero):
    if i%2==0:
        print(i,'es par')
    else:
        print(i, 'es impar')
