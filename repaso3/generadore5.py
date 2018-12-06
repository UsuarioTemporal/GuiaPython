# instruccion YIELD FROM

# Nos servira pra simplificar el código de los generadores en el caso de utilizar bucles anidados
 

# Matriz normal 
matriz=[[7,8,9],[4,5,6],[1,2,3]]

for subLista in matriz: 
    for item in subLista :
        print(item,end=" ")
    print()


# creacion desde cero
array,fila,columna= [],3,3
for i in range(fila) : 
    array.append([0]*columna) #creando subListas
print(array)

contador = 1
for f in range(fila) : 
    for c in range(columna) : 
        array[f][c]=contador
        contador+=1

for subLista in array : 
    for item in subLista : 
        print(item,end=" ")
    print()


# Usando generadores para simplificar los bucles anidados
def ciudades(*ciudades) : # Cuando se coloca un asterisco dentro de un argunmento esto significa 
                          # que puede recibir un numero indeterminado de elementos y que lo recibira en 
                          # forma de tupla
    for item in ciudades :
         yield item


ObjetoGeneradorCuidades = ciudades("Lima","Callao","Lurin","Villa el salvador")

print(next(ObjetoGeneradorCuidades))
print(next(ObjetoGeneradorCuidades))
print(next(ObjetoGeneradorCuidades))


# Uso del yield from
def paises(*paises) : 
    for item in  paises : 
        yield from item

ObjetogeneradorPaises = paises("Peru","Argentina","Bolivia")

print(next(ObjetogeneradorPaises))
print(next(ObjetogeneradorPaises))
print(next(ObjetogeneradorPaises))
print(next(ObjetogeneradorPaises))
print(next(ObjetogeneradorPaises))
print(next(ObjetogeneradorPaises))