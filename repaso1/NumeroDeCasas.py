import math
numeroDeCasas=int(input("Ingrese el número de casas"))
if numeroDeCasas < 8 :
    print("No exite casa que cumpla la condición : ")
else :
    casa = (numeroDeCasas**2 + numeroDeCasas)/2 
    valorEntero = int(math.sqrt(casa))
    casa = math.sqrt(casa) 
    if valorEntero == casa :
        print("La casa encontrada es ",valorEntero)
    else : 
        print("No existe casa que cumpla la condición")
