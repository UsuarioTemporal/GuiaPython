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
    def __init__(self, marca, modelo, llantas,caballito=False):
       super().__init__(marca, modelo, llantas)
       self.__caballito=caballito;
    def hacerCaballito(self):
        self.__caballito=True;
    def estadoActual(self):
        super().estadoActual()
        print(self.__caballito)

class VElectrico() :
    def __init__(self,cargado=False):
        self.__autonomia = 100
        self.__cargado=cargado
    def estadoActual(self):
        print(self.__autonomia+ " "+self.__cargado)


class Bicicleta(Vehiculo,VElectrico): # Se da precencia a la primera clase que se hereda
    
    def __init__(self, marca, modelo, llantas,cargado):
        Vehiculo.__init__(self,marca, modelo, llantas)
        VElectrico.__init__(self,cargado)
    def estadoActual(self):
        super().estadoActual()
        VElectrico.estadoActual(self)
        

miMoto =Moto("Honda","CBR",2)
miMoto.estadoActual()
miMoto.hacerCaballito()
miMoto.estadoActual()


print("Bici")
miBicicleta = Bicicleta("Bici","Bici",2,True) 
miBicicleta.estadoActual()