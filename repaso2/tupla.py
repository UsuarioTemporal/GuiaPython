"""
    Las tuplas son listas inmutables (no cambia), es decir no se puede modificar 
     * despues de su creacion .
     * no permiten añadir , eliminar, mover elementos etc (no append, remove)
     * si permiten extraer porciones, pero el resultado de la extraccion es un nueva tupla
     * si permiten comprobar si un elemento se encuentra en la tupla

     ¿ Qué utilidad o ventaja tienen respecto a las listas ? 
     * Mas rápidas 
     * menos espacio (mas optimizado)
     * formatean String 
     * pueden utilizarse como claves en un diccionario (las listas no)
"""
tupla = ("Hola",12,"como estas")
# tambien tupla = 15 ," sdasd" ,34 -- se conoce como empaquetado de tupla
#  desempaquetando tuplas 
hola = "hola"
numero = 12
tuplaEmpaquetada = hola,numero #empaquetando
hola,numero=tuplaEmpaquetada  #desempaquetando
tupla2 = ("Hola",12,"como estas")
# print(type(tupla))
print("Hola" in tupla)
print(tupla)
print(tupla[2])
print(tupla.index(12))
tupla3 =tupla +tupla2
print(tupla3)


#  Conversion para convertir una tupla a una lista y viseversa
lista = list(tupla3)
lista.append("que pex")
print(lista)

tupla4 =tuple(lista)
print(tupla4)