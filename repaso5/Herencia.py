class Vehiculo() :
    def __init__(self, marca,modelo):
        self.__marca = marca 
        self.__modelo=modelo
        self.__enMarcha=False
        self.__acelera=False
        self.__frna=False
    def arrancar(self) :
        self.__enMarcha=True
    def acelerar(self):
        self.__acelera=True
    def frenar(self):
        self.__frna=True
    def estadoActual(self):
        print(self.__modelo,self.__marca,self.__enMarcha,self.__acelera,self.__frna)



class Moto(Vehiculo) : #la clase moto hereda de la clase vehiculo
    pass

miMoto =Moto("Honda","CBR")
miMoto.estadoActual()

