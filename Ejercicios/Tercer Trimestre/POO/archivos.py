flujo=open('archivos/inicio.txt','a')       #Se crea una variable seguido del metodo open, donde se introducen los parametros tales como la ruta del archivo y el comando de accion que se va a realizar.
#datos=flujo.read()                         #Se crea otra variable que contenga la variable amterior con el metodo de leer el archivo.                            
#print(datos)                               #Se imprime la variable para mostrar los datos que tenia el archivo
flujo.write('\nCuando estudian con juicio') #Se utiliza el metodo Write para escribir y actualizar lo que contenga en el archivo.
datos=flujo.read()                          #Se crea la variable para utilizar la clase anterior y utilizar el metodo para leer, sin ningun parametro.
print(datos)                                #Se imprime la variable para mostrar los cambios.

#Se utiliza un tercer parametro para la codificacion de tildes y etc. 