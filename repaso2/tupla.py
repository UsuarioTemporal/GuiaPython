"""
    Las tuplas son listas inmutables (no cambia), es decir no se puede modificar 
     * despues de su creacion .
     * no permiten añadir , eliminar, mover elementos etc (no append, remove)
     * si permiten extraer porciones, pero el resultado de la extraccion es un nueva tupla
     * no permiten busquedas , no index
     * si permiten comprobar si un elemento se encuentra en la tupla

     ¿ Qué utilidad o ventaja tienen respecto a las listas ? 
     * Mas rápidas 
     * menos espacio (mas optimizado)
     * formatean String 
     * pueden utilizarse como claves en un diccionario (las listas no)
"""
tupla = ("Hola",12,"como estas")
# print(type(tupla))
print("Hola" in tupla)
print(tupla)
print(tupla[2])
print(tupla.index(12))