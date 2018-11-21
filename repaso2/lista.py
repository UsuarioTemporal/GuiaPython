lista=["Texto 1","texto 2",15,14]
lista.append("Carlos")
# Imprimer la lista completa
print(lista)
print(lista[:])


# desde 0 hast 2 pero este no lo toma es decir [0;2>
print(lista[0:2])
print(lista[0:])
print(lista[:3])

# lista.insert(8,23) lo curioso de esto es que es:
"""
    lo cursioso es que detecta la cantidad de datos
    y lo apila uno al lado de otro pero si insertamos 
    en el medio de una lista de una lista si existente
    lo añade , pero si lo colamos en un rango
    fuera de su lista lo apila al final
"""
print(lista)
lista.insert(2,23)
print(lista) #empura el dato hacia adelante 