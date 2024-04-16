#Son similares a las listas
#las tuplas no se pueden modificar, son inmutables
#si una tupla tiene un solo elemento, si o si tiene que terminar con coma => ('Naranja',)

frutas = ('Naranja', 'Banana', 'Manzana')
print(frutas)
print(len(frutas))
print('Manzana' in frutas)
print(frutas[0])
print(frutas[-1])
print(frutas[0:2])
for fruta in frutas:
    print(fruta, end=', ') #para que no salga el salto de linea por default

#cambiar valor tupla
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas = tuple(frutasLista)
print('\n',frutas)

#eliminar la tupla por completo
del frutas
print(frutas)