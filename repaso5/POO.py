class Auto() : 
    def __init__(self): # constructor
        self.__largoChasis = 250 # el guion abajo significa encapsulado "privado"
        self.__anchoChasis = 120 
        self.__ruedas = 4
        self.__enMarcha=False

    def arrancar(self,marchando): # el self hace referencia al propio objeto perteneciente 
                        #a la clase , con compraciones con otros lenguajes el self es igual
                        # que el this
        self.__enMarcha=marchando
        if self.__enMarcha :
            return "Encendido"
        else : 
            return "Apagado"
    def estado(self) : 
        print(self.__anchoChasis,self.__largoChasis,self.__ruedas,self.__enMarcha)

toyota = Auto()
sisan = Auto()

print(toyota.arrancar(False))
toyota.estado()
print(sisan.arrancar(True))
sisan.estado()
