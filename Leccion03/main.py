'''condicion = 10

if condicion == True:
    print('condición verdadera')
elif condicion == False:
    print('condicion falsa')
else:
    print('condición no reconocida')   
'''

'''
numero = int(input('Proporciona un valor entre 1 y 3:'))
numeroTexto = ''

if numero == 1:
    numeroTexto = 'Número uno'
elif numero == 2:
    numeroTexto = 'Número dos'
elif numero == 3:
    numeroTexto = 'Número tres'
else:
    numeroTexto = 'Valor fuera de rango'

print(f'Número proporcionado : {numero}: {numeroTexto}')
'''

'''
condicion = True


print('Condición verdadera') if condicion else print ('Condición falsa')
'''

mes = int(input('Proporciona mes del año (1-12): '))
estacion = None
if mes == 1 or mes == 2 or mes == 12:
    estacion = 'Verano'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Otoño'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Invierno'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Primavera'
else:
    estacion = 'Valor incorrecto'
print(f'Para el mes {mes} la estacion es: {estacion}')