def coincidencia(cadena) :
    for sub in cadena :
        if sub=="hola":
            yield sub

count = 0
cadena = 'hola que hola si uno'
cadena=cadena.split() # convirtiendo a lista 
for item in coincidencia(cadena) :
    count +=1 
print(count)