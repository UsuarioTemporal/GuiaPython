"""
    Los generadores en python nos van a servir para poder crer objetos sin necesidad de
    almacenarlos en la memoria ram los cuales se ven reflejados en codificaciones
    como el for ,donde encontramos el numero y el rango los cuales son un generador
    

"""



""" 
    cuando se utiliza yield from : se simplifica el código de los generadores en el caso de 
    utilizar bicles anidados
"""

x = (i for i in range(10))
for item in x :
    print(item)