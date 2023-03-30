import sqlite3                                                          #Se importa el modulo definido de sqlite
#con=sqlite3.connect('C:\\padilla\\sqlite-tools\\db\\pythondb.db')      #Ruta relativa
con=sqlite3.connect('pythonsqlite/pythondb.db')                         #Se crea una variable con el metedo .connect para la conexion con la base de datos con la ruta absoluta.
print(type(con))                                                        #Se imprime con el type el conector para mostrar la base da datos
micursor=con.cursor()                                                   #Se crea un cursor para apuntar a la base de datos
print(type(micursor))                                                   #Se imprime la variable micursor para ver si apunta a la base de datos.
new_sql="SELECT * from Persona;"                                        #Se crea una variable new_sql y entre comillas se utiliza la sentencia de SQL, que sirve para seleccionar todos los datos de la tabla creada.
micursor.execute(new_sql)                                               #Se ejecuta el cursor con execute para realizar la consulta escrita en la variable new_sql
lista=micursor.fetchall()                                               #Se crea una lista para el cursor y con .fetchall se selecciona todos los datos de la BD.
for fila in lista:                                                      #Se crea un for para recorrer todos los datos de la lista.
    print(fila[0])                                                      #Se imprime el primer dato que aparece en la fila
    print(fila[1])                                                      #Se imprime el segundo dato que aparece en la fila
    print(fila[2])                                                      #Se imprime el tercer dato que aparece en la fila
    print(fila[3])                                                      #Se imprime el cuarto dato que aparece en la fila.
    print('*'*50)                                                       #Se imprime un separador con 50 '*' para diferenciar cada dato del anterior
    
    
import sqlite3                                                          #Se importa slite
with sqlite3.connect('pythonsqlite/pythondb.db')as con:                 #se agrega un with as para conectar sqlite con la base de datos mediante la ruta absoluta del archivo.
    micursor=con.cursor()                                               #Se crea un cursor que va a apuntar a la base de datos indicada
    new_sql="SELECT first_name,id from persona where id>250"            #Se utiliza una sentencia SQL para ver el primer nombre de la tabla personas con un id mayor a 250.
    print(micursor.execute(new_sql).fetchall())                         #Se ejecuta la variable new_sql con fetchall para mostrar todos los datos seleccionados.