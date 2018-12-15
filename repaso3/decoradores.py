# los decoradores son funciones que reciben como parametro
#una funcion para poder retornar otra funcion
def decorador(func): 
    def nueva_funcion(): # esta funcion se encargara de ejecutar la funcion que 
                        # recibe como parametro
        print("Vamos a ejecutar la funcion")
        func()
        print("Se ejecuto la funcion")

    return nueva_funcion

@decorador
def saluda():
    print("Hola")

saluda()
