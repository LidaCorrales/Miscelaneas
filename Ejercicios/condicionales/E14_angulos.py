angulo = int(input("Ingresar angulo en grados: "))
radianes = 3.1416 * angulo / 180
vuelta = 0

if angulo >= 360:
    vuelta=angulo // 360
    angulo%=360
    if vuelta == 1:
        print("Se realizo", vuelta, "vuelta a la circunferencia")
    else:
        print("Se realizo", vuelta, "vuelta a la circunferencia")

if angulo >= 0 and angulo <= 90:
    print("Cuadrante 1.", radianes, "en radianes")
elif angulo > 90 and angulo <= 180:
    print("Cuadrante 2", radianes, "en radianes")
elif angulo > 180 and angulo <= 270:
    print("Cuadrante 3", radianes, "en radianes")
elif angulo > 270 and angulo <= 360:
    print("Cuadrante 4", radianes, "en radianes")