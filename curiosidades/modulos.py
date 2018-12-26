import monedas
import math

x= 5.74
print(math.floor(x))
print(math.ceil(x))
print(math.trunc(x))

print("Ingrese tipo de moneda y el valor de cambio [separados por una coma ,]",end=" ")
texto = str(input()).split(",")
tipoDeMoneda = texto[0]
valorCambio=float(texto[1])

monedas.definirTipoMoneda(tipoDeMoneda,valorCambio)
print("Ingrese el monto a convertir ",tipoDeMoneda," a USD ",end=" ")
monto=float(input())
resultado = monedas.convertir(monto,tipoDeMoneda)
print(monto," ",tipoDeMoneda," en USD es ",resultado)