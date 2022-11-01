#Escribir un algoritmo que pida un valor entero que equivale a una cantidad de DINERO y calcule a cuantos billetes
monto = int(input("Ingresar monto de dinero: "))
if monto >= 50000:
    dinero_restante = monto // 50000 
    print("Se necesita " + str(dinero_restante) + " billetes de 50.000 pesos")
    monto%=50000
#Se le asigna el if a cada valor de billete
if monto >= 20000:
    dinero_restante = monto // 20000 
    print("Se necesita " + str(dinero_restante) + " billetes de 20.000 pesos")
    monto%=20000

if monto >= 10000:
    dinero_restante = monto // 10000 
    print("Se necesita " + str(dinero_restante) + " billetes de 10.000 pesos")
    monto%=10000

if monto >= 5000:
    dinero_restante = monto // 5000 
    print("Se necesita " + str(dinero_restante) + " billetes de 5000 pesos")
    monto%=5000

if monto >= 2000:
    dinero_restante = monto // 2000 
    print("Se necesita " + str(dinero_restante) + " billetes de 2000 pesos")
    monto%=2000

if monto >= 1000:
    dinero_restante = monto // 1000 
    print("Se necesita " + str(dinero_restante) + " billetes de 1000 pesos")
    monto%=1000