class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):           #->mi_personaje = Personaje("Nombrexd",10,1,5,100)
        self.fuerza = self.fuerza + fuerza                          # mi_personaje.atributos()
        self.inteligencia = self.inteligencia + inteligencia        # mi_personaje.subir_nivel(1,2,0)
        self.defensa = self.defensa + defensa                       # mi_personaje.atributos()

    def esta_vivo(self):                                            # mi_personaje = Personaje("Nombrexd",10,1,5,100)
        return self.vida > 0                                        # print(mi_personaje.esta_vivo())

    def morir(self):                                                # mi_personaje = Personaje("Nombrexd",10,1,5,100)
        self.vida = 0                                               # mi_personaje.morir()
        print(self.nombre, "ha muerto")                             # mi_personaje.atributos()

    def daño(self, enemigo):                                        # mi_enemigo = Personaje("Enemigo",8,5,3,100)
        return self.fuerza - enemigo.defensa                        # print(my_personaje.daño(mi_enemigo))

    def atacar(self, enemigo):                                                              # mi_personaje = Personaje("Nombrexd",10,1,5,100)
        daño = self.daño(enemigo)                                                           # mi_enemigo = Personaje("Enemigo",8,5,3,100)
        enemigo.vida = enemigo.vida - daño                                                  # mi_personaje.atacar(mi_enemigo)
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)        # mi_enemigo.atributos()
        if enemigo.esta_vivo():                                                             
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()

#Encapsulacion
"""def get_fuerza(self):                                            # mi_personaje = Personaje("Nombrexd",10,1,5,100)
        return self.__fuerza                                        # mi_enemigo = Personaje("Enemigo",8,5,3,100)
                                                                    # print(mi_personaje.get_fuerza())
    def set_fuerza(self, fuerza):                                   
        if fuerza < 0:
            print ("Error haz introducido un error negativo")
        else:                                                       # mi_personaje.set_fuerza(-5)
            self.__fuerza = fuerza"""                               # mi_personaje.atributos()

#Herencia
class Guerrero(Personaje):
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):                            # nombreG = Guerrero("Bakugo",20,10,10,100,5)
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)                                   #nombreG.atrubutos()
        self.espada = espada                                                                            #super() --> LLamar atrubutos y metodos de la superclase sin tener que escribirla.

    def cambiar_arma(self):                                                                             # nombreG = Guerrero("Bakugo",20,10,10,100,5)
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10"))      # nombreG.cambiar_arma()
        if opcion == 1:                                                                                 # nombreG.atributos()
            self.espada = 8                                                                             # print(nombreG.espada)
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número de arma incorrecta")

    def atributos(self):
        super().atributos()
        print("·Espada:", self.espada)

    def daño(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa

class Mago(Personaje):                                                              # Goku = Perosnaje("Goku", 20,15,10,100)
                                                                                    # N = Guerrero("N", 20,15,10,100,5)
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):         # hola = Mago("Nombre", 20,15,10,100,5)
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)               # Goku.atacar(N)
        self.libro = libro                                                          # N.atacar(hola)

    def atributos(self):                                                            # Goku - N - hola. atributos()
        super().atributos()
        print("·Libro:", self.libro)

    def daño(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa

#Polimorfismo
def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre,":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de ", jugador_2.nombre,":", sep="")
        jugador_2.atacar(jugador_1)
        turno = turno + 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")

personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

personaje_1.atributos()
personaje_2.atributos()      

combate(personaje_1, personaje_2)