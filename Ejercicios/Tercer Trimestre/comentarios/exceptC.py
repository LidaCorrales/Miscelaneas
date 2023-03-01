def try_syntax(numerator, denominator):                         #Se crea una funcion llamada try_syntax, la cual contiene dos parametros.
    try:                                                            
        print(f'In the try block: {numerator}/{denominator}')   #Se contiene en el try, dentro de ella se imprime una frase con los dos parametros separados con un "/". Esto con la sintaxis con "f" para que pueda ser reconocido y ejecutado correctamente. 
        #quiero ver el resultado de la operacion en el print    #Para ver el resultado solo se tiene que poner la variable dentro del print --> print(f 'In the try block: {result}')
        result = numerator / denominator                        #Se crea una variable que divida el numerator con el denominator
    except ZeroDivisionError as zde:                            #Se pone en el except el error, seguido de renombrarlo como "zde".
        print(zde)                                              #Se imprime el error "zde"
    else:                                                       
        print('The result is:', result)                         #Se agrega un bloque else, el cual funciona cuando el error no se ejecuta. Imprime la frase con la funcion del resultado. 
        return result                                           #Se da retorno el resultado.
    finally:
        print('Exiting')                                        #finally imprime cuando el programa ha acabado de manera correcta y se da por finalizado. 
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11, 4))                                        #Se llama a la funcion por medio de un print y se ponen los datos de prueba o parametros para ejecutar la función.