"""
    repr debería devolver una cadena quepuede copiarse y pegase para construtir el estado exacto del objeto, mientras el str es útil para logginf y observing resultados de depuracion.
"""

from decimal import Decimal
a = Decimal(1.25)
print(str(a)) # muestra a el objeto en formato string
print(repr(a)) # muestra la representacion del objeto



class Vector:
    def __init__(self,*args):
        self.x=args[0]
        self.y=args[1]
        self.z=args[2]
    def __repr__(self):
        return 
    def __str__(self):
        return 