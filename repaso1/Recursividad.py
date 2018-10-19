def show(numTerm):
    if numTerm>0 :
        print("Hola mundo :v")
        return show(numTerm-1)
    return 

print("Hola mundo recursivamente")
terminos = int(input("Ingrese la cantidad de terminos : "))
show(terminos)