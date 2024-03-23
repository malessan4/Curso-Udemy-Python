print('Proporcione los siguientes datos del libro')
nombreLibro = input('Ingrese el nombre del libro: ')
print(nombreLibro)
libroId = int(input('Ingrese el ID del libro'))
print(libroId)
precio = float(input('Ingrese el precio del libro'))
print(precio)
envio = (input('Indica si es envio gratuito (si/no): '))
if envio == 'si':
    print('El libro se envia gratuitamente')
elif envio == 'no':
    print('El libro no se envia gratuitamente')
else:
    print('Valor incorrecto, debe escribir si/no')

print(f'''
    Nombre: {nombreLibro}
    Libro ID: {libroId}
    Precio: {precio}
    Envio gratuito: {envio}
''')