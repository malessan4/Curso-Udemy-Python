"""
Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado
# formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)

"""


def calcuImpuesto(pago, impuesto):
    pagoConImpuesto = pago + pago * (impuesto/100)
    return pagoConImpuesto

pago = float(input('Proporcione el pago sin impuesto: '))
impuesto = float(input('Proporcione el monto del impuesto: '))

pago_con_impuesto = calcuImpuesto(pago, impuesto)
print(f'Pago con impuesto: {pago_con_impuesto}')