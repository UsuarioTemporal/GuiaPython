# los decoradores son funciones que reciben como parametro
#una funcion para poder retornar otra funcion
def decorador(func): 
    def nueva_funcion(): # esta funcion se encargara de ejecutar la funcion que 
                        # recibe como parametro
        pass
    return nueva_funcion()

def saluda():
    print("Hola")
    
decorador(saluda())