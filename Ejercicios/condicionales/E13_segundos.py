pedir_segundos = int(input("Segundos que desea convertir: "))
minutos = 0
horas = 0

if pedir_segundos >= 3600:
    horas = pedir_segundos // 3600
    pedir_segundos%=3600
if pedir_segundos >= 60:
    minutos = pedir_segundos // 60
    pedir_segundos%=60

if horas == 1:
    print("La cantidad de segundos son: ", horas, "Hora", minutos, "Minutos y ", pedir_segundos, "Segundos")
elif minutos == 1:
    print("La cantidad de segundos son: ", horas, "Hora", minutos, "Minutos y ", pedir_segundos, "Segundos")
elif pedir_segundos == 1:
    print("La cantidad de segundos son: ", horas, "Hora", minutos, "Minutos y ", pedir_segundos, "Segundos")
else:
    print("La cantidad de segundos son: ", horas, "Hora", minutos, "Minutos y ", pedir_segundos, "Segundos")