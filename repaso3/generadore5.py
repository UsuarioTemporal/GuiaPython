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