import random 
num = 'f'*5
print(num)

def numeroParesParaNoHombres (numeroTerminos) :
    lista = []
    while numeroTerminos > 0 : 
        i = random.randint(0,100) 
        if i %2==0 :
            lista.append(i)
            numeroTerminos-=1
    return lista

# Con generadores como los machos . Chavex si ves esto recuerda que hago 
# este repositorio para que aprendas ,ya deja de trapear :v .Sabes de lo hablo
# piche trapo :v xdxdx
def numeroParesParaMachos(numeroTerminos):
    lista = []
    while numeroTerminos > 0 : 
        i = random.randint(0,100) 
        if i %2==0 :
            lista.append(i)
            numeroTerminos-=1
            yield lista
    


print(numeroParesParaNoHombres(int(input("Ingrese el número de terminos  : "))))


ObjetoIterable = numeroParesParaMachos(10)

for itemDeObjeto in ObjetoIterable :
    print(itemDeObjeto)


