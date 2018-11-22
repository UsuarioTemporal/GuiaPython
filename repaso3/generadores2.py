"""
    Los generadores en python nos van a servir para poder crer objetos sin necesidad de
    almacenarlos en la memoria ram los cuales se ven reflejados en codificaciones
    como el for ,donde encontramos el numero y el rango los cuales son un generador


"""

"""
    ejemplos enumarete , range
"""

""" 
    cuando se utiliza yield from : se simplifica el código de los generadores en el caso de 
    utilizar bicles anidados
"""

x = (i for i in range(10))
for item in x :
    print(item)

for item in enumerate("abs"):
    print(item)

lista = ["perro","gato","rata","burro"]

for x,y in enumerate(lista) : #x posicion e y valor
    if x%2==0:
        print(y)