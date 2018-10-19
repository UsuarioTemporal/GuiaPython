import math
numeroDeCasas=int(input("Ingrese el número de casas"))
if numeroDeCasas < 8 :
    print("No exite casa que cumpla la condición")
else :
    casa = (numeroDeCasas**2 + numeroDeCasas)/2 
    casa = math.sqrt(casa) // 1
    # si el número es entero has algo
    print(casa)