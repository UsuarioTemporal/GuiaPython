"""
    las excepsiones son errores que ocurren en tiempo de ejecución , tanto para la sintaxis
    o para envolver el resultado de un dato mal ingresado o mal enviado
"""
numero1 = 0 
numero2 = 0
try:
    print(numero1/numero2)
except ZeroDivisionError as err:
    print("Error cero")

cadena = "Dasdasdasd"
otroNumero = 0

try:
    print(cadena/otroNumero)
except BaseException as Err:
    print("Error de tipo ",Err.__class__)
    

