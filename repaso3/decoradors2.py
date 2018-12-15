def decorador(func):
    def nuevaFuncion(*args):
        func(*args)
    return nuevaFuncion

@decorador
def suma(numer1,numero2):
    print(numer1+numero2)

suma(7,2)

#######################################
def decorator(func):
    def beforeAction():
        print("Antes de ejecutar")
    def afterAction():
        print("Despues de ejecutar")
    beforeAction()
    def newFunction(*args):
        re = func(*args);
        afterAction()
        return re
    return newFunction

@decorator
def suma(var1,var2):
    return var1+var2

print(suma(7,8))