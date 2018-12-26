divisas = {"PEN":3.256,"MXM":20}

def definirTipoMoneda(tipoMoneda,valor) :
    divisas[tipoMoneda]=valor
    return

def convertir(montoInicial,tipoMoneda="PEN") :
    valor=divisas.get(tipoMoneda)
    montoInicial/=valor
    return montoInicial

