#----->Ejercicio donde se ingrese un año y un mes con inputs, para mostrar el calendario de este mes

import calendar

anio = int(input("Ingrese el año: "))
mes = int(input("Ingrese el mes (1-12): "))
print(calendar.month(anio, mes))

#-----> crear una funcion que muestre los años bisiestos de un determinado rango de años sin usar el modulo isleadays

def mostrar_anios_bisiestos(anio_inicial, anio_final):
    anios_bisiestos = []
    for anio in range(anio_inicial, anio_final + 1):
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            anios_bisiestos.append(anio)
    return anios_bisiestos


#---->Ingresar fecha y que devuelva el dia de la semana (Lunes, Martes)

import datetime

fecha = input("Ingrese una fecha (formato: DD/MM/AAAA): ")
fecha_dt = datetime.datetime.strptime(fecha, "%d/%m/%Y")
dia_semana = fecha_dt.strftime("%A")
print(f"La fecha {fecha} corresponde al día de la semana {dia_semana}.")

#----->Hacer codigo que muestre los años bisiestos que tuvieron lugar desde 1970 hasta el presente año

import datetime
import calendar

anio_actual = datetime.datetime.now().year
anios_bisiestos = calendar.leapdays(1970, anio_actual)

for i in range(anios_bisiestos):
    anio_bisiesto = 1970 + i * 4
    if anio_bisiesto <= anio_actual:
        print(anio_bisiesto)

#--->Hacer un codigo en python que imprima el dia y el mes. Tambien imprima el mismo mes pero con la semana que inicia e domingo con lista de
#semanas del mes. 

import calendar

mes_actual = datetime.datetime.now().month
anio_actual = datetime.datetime.now().year
print(calendar.month_name[mes_actual], anio_actual)

semanas_del_mes = calendar.monthcalendar(anio_actual, mes_actual)
for semana in semanas_del_mes:
    print(semana)
