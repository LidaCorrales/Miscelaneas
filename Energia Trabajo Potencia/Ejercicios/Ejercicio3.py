#Calcular la potencia de una grúa que es capaz de levantar 60 bultos
#  de cemento hasta una altura de 2.5 metros en un tiempo de 2 segundos,
#  si cada bulto tiene una masa de 50 kg

def potencia_mecanica():
    ecuacion = masa*60*9.8*altura//tiempo
    return ecuacion

masa = int(input("Ingresar masa de bultos: "))
altura = float(input("Ingresar altura: "))
tiempo = int(input("Ingresar tiempo: "))
solucion = potencia_mecanica
print(potencia_mecanica(), "Jules")