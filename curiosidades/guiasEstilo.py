"""Para programar en python existe convenciones
en la escritura del código"""

# estas convenciones se usan para la legibilidad 
# del código y hacerlo entendible y consistente 


"""
 Citando del documenento PEP 8 : 
    Una guía de estilo se trata de consistencia. La consistencia con esta
    guía es importante. La consistencia dentro de un proyecto es más
    importante. La consistencia dentro de un módulo o función es aún
    más importante.

"""


# Razones por la cual romper las reglas de la consistencia en python u otro lenguaje

# Cuando el código se haga muy tecnico abarcando los lenguajes sencillos de leer 
# Cuando se trata de hacer eficiente el codigo , en ocaciones de rompe la consistencia



# DISEÑO

# USO DE LOS TABS PARA LA IDENTACIÓN , NO ESPACION
# MODIFICANDO TU EDITOR A LA IDENTACION CON 4 ESPACION , MAS NO 8 COMO VIENE POR DEFECTO EN OTROS IDE O EDITORES
def funcion1() : 
    return 3;# identacion con 4 espacios
def funcion2() : 
        return 4; #identacion por defecto 

def funcion3(request,http,#....
            var_integer) : # saltos para mejor entendimiento
    return request ; 

