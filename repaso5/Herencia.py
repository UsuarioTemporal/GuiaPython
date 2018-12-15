class Vehiculo() :
    def __init__(self, marca,modelo,llantas):
        self.__marca = marca 
        self.__modelo=modelo
        self.__enMarcha=False
        self.__acelera=False
        self.__frna=False
        self.__llantas=llantas
        
    def arrancar(self) :
        self.__enMarcha=True
    def acelerar(self):
        self.__acelera=True
    def frenar(self):
        self.__frna=True
    def estadoActual(self):
        print(self.__modelo,self.__marca,self.__enMarcha,self.__acelera,self.__frna,self.__llantas)



class Moto(Vehiculo) : #la clase moto hereda de la clase vehiculo
    def __init__(self, marca, modelo, llantas):
       super().__init__(marca, modelo, llantas)

miMoto =Moto("Honda","CBR",2)
miMoto.estadoActual()

