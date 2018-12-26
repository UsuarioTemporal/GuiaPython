from Persona import Persona
from Rebelde import Rebelde
class Estudiante(Persona,Rebelde):
    def __init__(self,nombre,nota=0,soyRebelde=False):
        Persona.__init__(self,nombre)
        self.__nota=nota
        Rebelde.__init__(self,soyRebelde)
        
    def mostrarDatos(self):
        super().mostrarDatos()
        print(self.__nota)
        Rebelde.mostrarDatos(self)

