try:                                        #Se comienza añadiendo un bloque de try donde se contienen datos correspondientes al error SyntaxError.
    #print(1/1))
    raise SyntaxError                       #Cuando llamamos raise, estamos pidiendo que se ejecuten un error de Syntaxerror. 
except SyntaxError as e:                    #Ponemos el except con el error mencionado y lo nombramos "e".
    print(e)                                #Imprime el except con el error recientemente llamado "e".
    print('Cierra el parentesis')           #Si el except se ejecuta, imprime la cadena contenida.
    

try:                                        #Se crea un try
    #raise ZeroDivisionError            
    print(1/0)                              #Se imprime el valor que vamos a probar para ver si hay error.
#except (ZeroDivisionError) as e:
except ZeroDivisionError as zde:            #Poner el except con el error que vamos a probar, nombrandolo como "zde"
    print(zde)                              #Cuando se de el except, imprime el error nombrado como "zde"
    #print('prueba error')