values = (1, 0)                                 #se pone una variable que almacena dos numeros.
#x,y=10,12
#print(divmod(10,3))
try:                                            #se inserta el bloque try
    q, r = divmod(*values)                      #se ponen dos variables para ser divididas por la funcion divmod, llamando a la variable values con * para que divida
    #print('valor de q=',q)                     #todos los valores que se contienen en esta.
    print(f'q={q}')                             #imprime el valor de q, con esta sintaxis se puede poner la variable adentro del texto. Poniendo "f" al principio para que se pueda reconocer esta sintaxis y ejecutar correctamente.
    print(f'r={r}')                             #Lo mismo pasa como la anterior linea, solo que la variable en esta linea es la r.
except (ZeroDivisionError, TypeError) as e:     #Se pone un except con los dos errores que queremos probar contenidos en un parentesis y separandolos por comas. Despues se le nombra a los errores "e".
    print(type(e), e)                           #Se imprime el tipo de error que genero, seguido del nombre del error y la justificacion del mismo.