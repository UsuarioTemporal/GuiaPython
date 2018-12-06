def dividir() : 
    try:
        numero1 = float(input("Primer numero : "))
        numero2 = float(input("Segundo numero : "))

        print("La division es  ",(numero1/numero2)," .")
    # print("La division es  "+str(numero1/numero2))
    #excepcion general no recomendable 
    # except :
    #     print("Ha ocurrido un error")
    except ValueError :
        print("Error de tipo")
    except ZeroDivisionError :
        print("No se puede dividir por cero")

dividir()