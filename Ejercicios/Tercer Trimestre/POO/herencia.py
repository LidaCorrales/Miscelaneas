class Vehiculo:                                                     #Se define una superclase o clase padre llamada vehiculo
    def __init__(self,tipo):                                        #Se da inicio con un constructor con su correspondiente self y un parametro llamado tipo
        self.tipo=tipo                                              #Se inicializa el atributo con el self llamando a tipo.
    def descripcion(self):                                          # se contruye un metodo con el parametro self
        print('Soy generico no tengo descripcion',self.tipo)        # se imprime la cadena con el metodo tipo, para que se muestre
#v=Vehiculo('Cualquier tipo')

    def getTipo(self):                                              # Se pone un getter con el parametro self
        return self.tipo                                            # se retorna el metodo de tipo 
        #return Vehiculo.tipo
    def __str__(self):                                              # Se pone un str para retornar valores con cadenas
        return 'Soy objeto de la clase Vehiculo'                    # Se retorna la cadena que se quiere mostrar

class Herramienta:                                                  # Se crea una subclase llamada herramienta
    def __init__(self,proposito):                                   # Se construye un constructor con el parametro self y uno llamado proposito
        self.__proposito=proposito                                  # Se incilaliza el atributo con el self para proposito
    def getProposito(self):                                         # Se pone un getter con el parametro self
        return self.__proposito                                     # Se retorna el atributo proposito para mostrarlo
    def __str__(self):                                              # Se crea un metodo str con el parametro self, polimorfismo
        return 'Soy objeto de la clase Herramienta'                 # Se retorna la cadena que se mostrara
class Terrestre(Vehiculo,Herramienta):                              # Se crea una subclase o clase hija, con los parametros de las dos superclases.
    def __init__(self,tipo,proposito):                              # Se pone un constructor con los parametros de la superclase
        Herramienta.__init__(self,proposito)                        # Se llama a la superclase Herramienta como atributo con las parametros de esa clase.
        Vehiculo.__init__(self,tipo)                                # Se llama a la siguiente superclase como atributo con los parametros de esa clase.
    def datos(self):                                                # Se crea un metodo llamado datos con el parametro self
        print('Tipo: ',super().getTipo())                           # Se imprime la cadena que va a mostrar con el metodo super(el cual se utiliza para llamar a la superclase sin escribirla) y el getter de tipo
        print('Tipo: ',super().getProposito())                      # Se imprime la cadena con el metodo super y el getter de proposito
    # def __str__(self):
    #     return 'Soy objeto de la clase Terrestre'
               
t=Terrestre("terrestre","carga")                                    # Se llama a la subclase Terrestre y se colocan los parametros requeridos
t.datos()                                                           # Se llama al metodo datos
print(t.__str__())                                                  # Se imprime el metodo str que heredo Terreste. (polimorfismo: ya que peude variar dependiendo de la clase que se tome)