def edad():                                             #Se crea una funcion llamada edad con ningun parametro.
    try:
        tuedad=int(input("introduce tu edad"))          #se crea una variable que pida por teclado un numero entero.
        print(f'tu edad es  {tuedad}')                  #Imprime la cadena junto con la variable anterior. Esto con la sintaxis de poner la variable dentro de la cadena, poniendo "f" al principio para reconocerlo y ejecutarlo.
        #print('Tu edad es ',tuedad)
    except ValueError as e:                             #se pone en el except el error mencionado y se renombra como "e".
        print(e)                                        #Se imprime el error.
        print("La edad debe ser un valor numerico...")  #Se imprime una cadena con la frase determinada cuando se ejecute el except.
        edad()                                          #Recursividad: La funcion se llama asi misma. Por lo cual, cada que termine la funcion, se vuelve a repetir hasta que se ponga un valor válido en la variable.
    
edad()                                                  #Se llama la funcion.