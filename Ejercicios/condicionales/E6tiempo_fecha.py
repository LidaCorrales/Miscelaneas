#Pida un numero al usuario que representa días del año.
D = int(input("Registre el dia del año: "))

if D>0 and D <=31:
    print("Mes de enero")
elif D >=32 and D <=59:
    print("Mes de febrero")
elif D >=60 and D <=90:
    print("Mes de marzo")
elif D >=91 and D <=120:
    print("Mes de abril")
elif D >=121 and D <=151:
    print("Mes de mayo")
elif D >=152 and D <=181:
    print("Mes de junio")
elif D >=182 and D <=212:
    print("Mes de julio")
elif D >=213 and D <= 243:
    print("El mes de agosto")
elif D >=244 and D <= 273:
    print("Mes de septiembre")
elif D >= 274 and D <= 304:
    print("Mes de octubre")
elif D >=305 and D <= 334:
    print("Mes de noviembre")
elif D >=335 and D <=365:
    print("Mes de Diciembre")
else:
    print("El numero no es valido")