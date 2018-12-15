# los decoradores son funciones que reciben como parametro
#una funcion para poder retornar otra funcion
def decorador(func): 
    def nueva_funcion():
        pass
    return nueva_funcion()

def saluda():
    print("Hola")