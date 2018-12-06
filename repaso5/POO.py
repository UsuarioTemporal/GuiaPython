class Auto() : 
    largoChasis = 250
    anchoChasis = 120 
    ruedas = 4
    enMarcha=False

    def arrancar(self): # el self hace referencia al propio objeto perteneciente 
                        #a la clase , con compraciones con otros lenguajes el self es igual
                        # que el this
        self.enMarcha=True

    def estado(self) : 
        if self.enMarcha : 
            return "Encendido"
        else : 
            return "Apagado"


toyota = Auto()
toyota.arrancar()
print(toyota.largoChasis)
print(toyota.anchoChasis)
print(toyota.ruedas)
print(toyota.enMarcha)
print(toyota.estado())