
"""
    Principio de sustitución : 
        un objeto de la subclase , siempre sera un objeto de la superclase
        Es decir que un que un Empleado es simpre una Persona
"""
# thom=Empleado()
# isinstance(thom,Empleado) # True
# isinstance(thon,Persona) # True


"""
    Polimorfismo : EL objeto se adpatara al tipo de instancia
"""
class Coche() :
    def desplazamiento(self) :
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo en dos ruedas")


class Camion():
    def desplazamiento(self):
        print("Me desplazo en seis ruedas ruedas")
 
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miObjeto = Moto()
desplazamientoVehiculo(miObjeto)