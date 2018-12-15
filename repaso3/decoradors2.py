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
    def newFunction(*args):
        res=func(*args)
        return res
    return newFunction

@decorator
def suma(var1,var2):
    return var1+var2

res = suma(7,8)
print(res)