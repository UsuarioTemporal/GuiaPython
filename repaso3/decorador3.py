def decorator(isValid=True) :
    def _decorator(func) :
        def beforeAction():
            print("Antes de la accion")
        def afterAction():
            print("Despues de la accion")
        def newFunction(*args):
            if isValid :
                beforeAction()
            
            return func(*args)
        afterAction()
        return newFunction
    return _decorator

@decorator(False)
def suma(numero1=0,numero2=0):
    return numero1+numero2

print(suma(1))
print(suma())
print(suma(11,3))