"""
    repr debería devolver una cadena que puede copiarse y pegase para construtir el estado exacto del objeto, mientras el str es útil para logginf y observing resultados de depuracion.
"""

from decimal import Decimal




class Vector:
    def __init__(self,args):
        self.x=args[0]
        self.y=args[1]
        self.z=args[2]
    
    def __str__(self):
        return f"x: {self.x!r}, y: {self.y!r}, z: {self.z!r}"

    def __repr__(self):
        return "Vector3([{},{},{}])".format(self.x, self.y, self.z)


if __name__=='__main' : #es este el script principal?
    pass

"""
    __repr__ : La representacion del objeto python generalmente lo convertira de nuevo a ese objeto
"""

a = Decimal(1.25)
print(str(a)) # muestra a el objeto en formato string
print(repr(a)) # muestra la representacion del objeto


v = Vector([1,2,3])
print(repr(v))
print(str(v))