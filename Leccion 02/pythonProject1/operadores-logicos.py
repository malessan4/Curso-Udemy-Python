"""
operador and: devuelve true si ambos operandos son True |a and b|
operador or: devuelve true si alguno de los operandos es true |a or b|
operador not: devuelve true si alguno de los operandos es false |not a|

a = True
b = False

resultado = a and b
# print(resultado)

resultado = a or b
# print(resultado)

resultado = not a
print(resultado)
"""

valor = int(input('Escribe el valor: '))
valorMinimo = 0
valorMaximo = 5

dentroRango = (valor >= valorMinimo) and (valor <= valorMaximo)

if dentroRango:
    print(f'El valor {valor} esta dentro de rango')
else:
    print(f'El valor {valor} esta afuera de rango')
