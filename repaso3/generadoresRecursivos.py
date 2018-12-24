

def recursive_generator(lis):
    if lis:
        yield lis[0]
        yield from recursive_generator(lis[1:]) 
"""
    al usar el yield nos enviará un valor , en este caso la primera posicion y lo alamcenara en un objeto iterable pero , como se ve en la parte de abajo lo se estara imprimiendo y cuando regresa a la funcion :
    si es que solo agregamos el yield recursive_generator(lis[1:])
    nos enviara toda la lista apartir de la posicion 1 

    pero nosostross quemos recorrer a partir de esa posicion , entonces usaremos el yield from
"""



for item in recursive_generator([6,3,9,1]):
    print(item,end=' ')