#obtener el factorial del numero 5

# 5! = 5 * 4 * 3 * 2 *1
# 5! = 5 * 4 * 3 * 2
# 5! = 5 * 4 * 6
# 5! = 5 * 24
# 5! = 120

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)

numero = int(input('ingresa un numero: '))   
resultado = factorial(numero)
print(f'El factorial de {numero} es {resultado}')