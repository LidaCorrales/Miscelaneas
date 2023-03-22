#Primero
import csv                                                  #Se importa elmodulo csv
header=['Fruit','Price']                                    #Se crea la variable header para crear el encabezado del archivo
rows=[['Apple',1200],                                       #Se crea las columnas para almacenar los datos
      ['Berry',2000],
      ['Lemon',1000],
      ['Melon',3000],
      ['Grapes',4000],
      ['Pear',2000]]

with open ('archivos/example.csv','w') as csvfile:          #Se crea un stream para crear un archivo y escribir en el.
    csvwriter=csv.writer(csvfile)                           #Se crea una variable para utilizar el metodo csv.writer y almacenar los datos en ella.
    csvwriter.writerow(header)                              #Se utiliza el metodo para escribir el titulo almacenado en la variable
    csvwriter.writerows(rows)                               #Se utiliza el metodo para escribir las columnas almacenadas en la variable
    
#Segundo
import csv                                                  #Se importa el modulo csv
diccio=[                                                    #Se crea un diccionario con los datos que se quieren escribir.
    {'name':'Alice','age':18},
    {'name':'Bob','age':19},
    {'name':'John','age':17}
]
header=['name','age']                                       #Se crea una variable para agregar el titulo

with open('archivos/people.csv','w') as csvfile:            #Se crea un stream con el archivo
    writer=csv.DictWriter(csvfile,fieldnames=header)        #Se crea una variable para utilizar el metodo especial para el diccionario y agregar los datos. Entre parentesis se le especifican las variables a almacenar
    writer.writeheader()                                    #Se utiliza el metodo para almacenar el header
    writer.writerows(diccio)                                #Se utiliza el metodo para almacenar los datos de la variable diccionario