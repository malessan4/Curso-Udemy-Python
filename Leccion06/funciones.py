#definir una función

#el nivel de tabulacion corresponde a la función
def miFuncion(nombre, apellido):
    print('saludos desde mi función')
    print(f'Nombre: {nombre}, Apellido: {apellido}')
    
miFuncion('Juan', 'Perez')
miFuncion('Carla', 'Lara')

#en el return es opcional el parentesis en este caso
def sumar(a = 0, b = 0):
    return a + b

resultado = sumar()
print (f'Resultado de la suma: {resultado}')

print (f'Resultado sumar: {sumar(2,8)}')