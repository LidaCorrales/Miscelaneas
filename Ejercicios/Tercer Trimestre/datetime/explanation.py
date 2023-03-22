#------> OBTENER LA FECHA ACTUAL Y CREAR OBJETOS DEL TIPO DE FECHA

#Una de las clases proporcionadas por el módulo datetime es una clase llamada date.
# Los objetos de esta clase representan una fecha que consta de año, mes y día.

#El método today devuelve un objeto del tipo date que representa la fecha local actual.

#Para crear un objeto date, debes pasar los parámetros año, mes y día:

"""from datetime import date

my_date = date(2019, 11, 4)
print(my_date)"""

#Ejemplo
"""from datetime import date

today = date.today()

print("Hoy:", today)
print("Año:", today.year)
print("Mes:", today.month)
print("Día:", today.day)"""

#-------> CREACION DE UN OBJETO DE FECHA A PARTIR DE UNA MARCA DEL TIEMPO

#La clase date nos da la capacidad de crear un objeto del tipo fecha a partir de una marca de tiempo.
#En Unix, la marca de tiempo expresa el número de segundos desde el 1 de Enero de 1970 
#a las 00:00:00 (UTC). Esta fecha se llama la época Unix, porque es cuando comenzó el conteo del tiempo en los sistemas Unix.

#La marca de tiempo es en realidad la diferencia entre una 
#fecha en particular (incluida la hora) y el 1 de enero de 1970, 00:00:00 (UTC), expresada en segundos.

#Para crear un objeto de fecha a partir de una marca de tiempo,
# debemos pasar una marca de tiempo Unix al método fromtimestamp.

#podemos usar el módulo time, que proporciona funciones relacionadas con el tiempo.
#Uno de ellos es una función llamada time(), que devuelve el número de segundos desde
#el 1 de enero de 1970 hasta el momento actual en forma de número flotante.

"""from datetime import date
import time

timestamp = time.time()
print("Marca de tiempo:", timestamp)

d = date.fromtimestamp(timestamp)
print("Fecha:", d)"""

#---------> OBJETO DE FECHA USANDO EL FORMATO ISO
#El módulo datetime proporciona varios métodos para crear un objeto date. Uno de ellos es el método fromisoformat,
#que toma una fecha en el formato AAAA-MM-DD compatible con el estándar ISO 8601.

"""from datetime import date

d = date.fromisoformat('2019-11-04')
print(d)"""

#------> EL METODO REPLACE()
#A veces, es posible que debas reemplazar el año, el mes o el día con un valor diferente.
#No puedes hacer esto con los atributos de año, mes y día porque son de solo lectura. 
#En este caso, puedes utilizar el método llamado replace.

"""from datetime import date

d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)"""

#------> WEEKDAY
#evuelve el día de la semana como un número entero, donde 0 es el Lunes y 6 es el Domingo. 

"""from datetime import date

d = date(2019, 11, 4)
print(d.weekday())"""

#La clase date tiene un método similar llamado isoweekday, que también
# devuelve el día de la semana como un número entero, pero 1 es Lunes y 7 es Domingo:

"""from datetime import date

d = date(2019, 11, 4)
print(d.isoweekday())"""

#--------> CREANDO OBJETOS TIME
#Clase que permite presentar la hora.
#Parametros: time(hour, minute, second, microsecond, tzinfo [zonas horarias], fold [el tiempo de pared es el tiempo real])

"""from datetime import time

t = time(14, 53, 20, 1)

print("Tiempo:", t)
print("Hora:", t.hour)
print("Minuto:", t.minute)
print("Segundo:", t.second)
print("Microsegundo:", t.microsecond)"""

#------>FUNCIONES MODULO TIME
#el uso de la función sleep, que suspende la ejecución del programa por el determinado número de segundos.
#la función sleep acepta solo un número entero o de punto flotante.

"""import time

class Student:
    def take_nap(self, seconds):
        print("Estoy muy cansado. Tengo que echarme una siesta. Hasta luego.")
        time.sleep(seconds)
        print("¡Dormí bien! ¡Me siento genial!")

student = Student()
student.take_nap(5)"""

#La función ctime devuelve una cadena para la marca de tiempo pasada.
#ctime, que convierte el tiempo en segundos desde el 1 de enero de 1970 (época Unix) en una cadena.

"""import time

timestamp = 1572879180      #la marca de tiempo expresa el 4 de noviembre de 2019 a las 14:53:00
print(time.ctime(timestamp))"""

#También es posible llamar a la función ctime
#sin especificar el tiempo en segundos. En este caso, se devolverá la hora actual.

"""import time
print(time.ctime())"""

#las funciones gmtime() y localtime()

#la clase struct_time
#time.struct_time:
    #tm_year   # Especifica el año.
    #tm_mon    # Especifica el mes (valor de 1 a 12)
    #tm_mday   # Especifica el día del mes (valor de 1 a 31)
    #tm_hour   # Especifica la hora (valor de 0 a 23)
    #tm_min    # Especifica el minuto (valor de 0 a 59)
    #tm_sec    # Especifica el segundo (valor de 0 a 61)
    #tm_wday   # Especifica el día de la semana (valor de 0 a 6)
    #tm_yday   # Especifica el día del año (valor de 1 a 366)
    #tm_isdst  # Especifica si se aplica el horario de verano (1: sí, 0: no, -1: no se sabe)
    #tm_zone   # Especifica el nombre de la zona horaria (valor en forma abreviada)
    #tm_gmtoff # Especifica el desplazamiento al este del UTC (valor en segundos)

"""import time

timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))"""

#Las funciones asctime() y mktime()

#llamada asctime, convierte un objeto struct_time o una tupla en una cadena.
#Toma en cuenta que la conocida función gmtime se usa para obtener el objeto struct_time.
#Si no se proporciona un argumento a la función asctime, se utilizará el tiempo devuelto por la función localtime.

#La segunda función llamada mktime convierte un objeto struct_time o una tupla que
#expresa la hora local al número de segundos desde la época de Unix.

#2019 => tm_year
#11 => tm_mon
#4 => tm_mday
#14 => tm_hour
#53 => tm_min
#0 => tm_sec
#0 => tm_wday
#308 => tm_yday
#0 => tm_isdst

"""import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))"""

#------>CREACION DE OBJETOS DATETIME
#En el módulo datetime, la fecha y la hora se pueden representar como objetos separados
#o como un solo objeto. La clase que combina fecha y hora se llama datetime.

#datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)

"""from datetime import datetime

dt = datetime(2019, 11, 4, 14, 53)

print("Fecha y Hora:", dt)
print("Fecha:", dt.date())
print("Hora:", dt.time())"""

#--------->METODOS QUE DEVUELVEN LA FECHA Y HORA ACTUAL

#today(): devuelve la fecha y hora local actual con el atributo tzinfo establecido a None.
#now(): devuelve la fecha y hora local actual igual que el método today, a menos que le 
#   pasemos el argumento opcional tz. El argumento de este método debe ser un objeto de la subclase tzinfo.
#utcnow(): devuelve la fecha y hora UTC actual con el atributo tzinfo establecido a None.

"""from datetime import datetime

print("hoy:", datetime.today())
print("ahora:", datetime.now())
print("utc_ahora:", datetime.utcnow())"""

#----------> OBTENER MARCA DEL TIEMPO

#El método timestamp devuelve un valor flotante que expresa el número de segundos transcurridos
#  entre la fecha y la hora indicadas por el objeto datetime y el 1 de enero de 1970, 00:00:00 (UTC).

"""from datetime import datetime

dt = datetime(2020, 10, 4, 14, 55)
print("Marca de tiempo:", dt.timestamp())"""

#--------> FORMATO DE FECHA Y HORA 
# strftime: Método nos permite devolver la fecha y la hora en el formato que especificamos.
#El método strftime toma solo un argumento en forma de cadena que especifica un formato que puede constar de directivas.

#Una directiva es una cadena que consta del carácter % (porcentaje) y una letra minúscula o mayúscula.
#%Y: devuelve el año con el siglo como número decimal. En nuestro ejemplo, esto es 2020.
#%m: devuelve el mes como un número decimal con relleno de ceros. En nuestro ejemplo, es 01.
#%d: devuelve el día como un número decimal con relleno de ceros. En nuestro ejemplo, es 04.

"""from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))"""

#La directiva %Y devuelve el año sin siglo como un número decimal con relleno de ceros.
#La directiva %B devuelve el mes como el nombre completo.

"""from datetime import time
from datetime import datetime

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))"""

#----->La función strftime() en el módulo time
#Se diferencia ligeramente de los métodos strftime en las clases proporcionadas por el
#  módulo datetime porque, además del argumento de formato, también puede tomar
#  (opcionalmente) un objeto tuple o struct_time.

"""import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))"""

#------->LE METODO STRPTIME()
#A diferencia del método strftime, crea un objeto datetime a partir de una cadena que representa una fecha y una hora.
#l método strptime requiere que especifiques el formato en el que guardaste la fecha y la hora.

"""from datetime import datetime
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))"""

#En el módulo time, puedes encontrar una función llamada strptime, que analiza una cadena que representa
#  un tiempo en un objeto struct_time. Su uso es análogo al método strptime en la clase datetime

"""import time
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))"""

#---------> OPERACION DE FECHA Y HORA
#Para crear un objeto timedelta, simplemente realiza una resta en los objetos date o datetime.

"""from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)"""

#--------> CREACION DE OBJETOS TIMEDELTA
#También puede crear un objeto tu mismo. Para ello, vamos a familiarizarnos con los argumentos aceptados por
#  el constructor de la clase, que son:days, seconds, microseconds, milliseconds, minutes, hours, y weeks.
#  Cada uno de ellos es opcional y el valor predeterminado es 0.

"""from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)"""

#El objeto timedelta se puede multiplicar por un número entero
#Otra operación interesante usando el objeto timedelta es la suma.
#Como resultado de estas operaciones, recibimos objetos date y datetime
#  incrementados en días y horas almacenados en el objeto timedelta.

#La operación de multiplicación presentada te permite aumentar rápidamente el valor del objeto timedelta,
#  mientras que la multiplicación también puede ayudar a obtener una fecha en el futuro.

"""from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)"""