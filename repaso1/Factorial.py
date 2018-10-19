def factorial(numero):
    if numero == 0:
        return 1
    return numero * factorial(numero-1)

print("Ingrese el número para calcular el factorial : ")
numero = int(input())
print("El factorial del número ",numero," es : ",factorial(numero))