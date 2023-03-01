#Solicite al usuario la hora en formato hh:mm:ss (hora militar, 24 horas). El programa debe responder que hora será un segundo después.
horas = int(input("Ingresar horas en formato militar: "))
minutos = int(input("Ingresar minutos en formato militar: "))
segundos = int(input("Ingresar segundos en formato militar: "))

if segundos >58:
    segundos=00
    minutos+=1
    if minutos>58:
        minutos=00
        horas+=1
        if horas>23:
            horas=00
            print("Hora en un segundo despues es:", horas, ":", minutos, ":", segundos)
        else:
            print("Hora en un segundo despues es:", horas, ":", minutos, ":", segundos)
    else:
        print("Hora en un segundo despues es:", horas, ":", minutos, ":", segundos)
else:
    segundos+=1
    print("Hora en un segundo despues es:", horas, ":", minutos, ":", segundos)