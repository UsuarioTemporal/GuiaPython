def decorador(func):
    def nuevaFuncion(*args):
        func(*args)
    return nuevaFuncion

@decorador
def suma(numer1,numero2):
    print(numer1+numero2)

suma(7,2)