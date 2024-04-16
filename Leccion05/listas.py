#Definir una lista de tipo str
nombres = ['Juan','Carla','Ricardo','Maria']
#imprimir la lista de nombres
print(nombres)

#acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])

#acceder a los elementos de forma inversa
print(nombres[-1])
print(nombres[-2])

#imprimir un rango
print(nombres[0:2])

#ir del inicio de la lista al indice (sin incluirlo)
print(nombres[:3])

#desde el indice indicado hasta el final
print(nombres[1:])

#cambiar un valor
nombres[3] = 'Ivone'
print(nombres)

#iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existe más nombres en la lista')
    
#preguntar el largo de una lista
print(len(nombres))

#preguntar si se encuentra tal elemento
print('Juan' in nombres)
#devuelve valor booleano

#agregar un elemento a la lista, va a ser el ultimo de la lista
nombres.append('Lorenzo')
print(nombres)

#insertar un elemento en un índice en especifico
nombres.insert(1, 'Octavio')
print(nombres)

#remover un elemento, tiene que ser si o si por valor y no por indice
nombres.remove('Octavio')
print(nombres)

#remover el último valor agregado
nombres.pop()
print(nombres)

#eliminar un indice
del nombres[0]
print(nombres)

#limpiar la lista
nombres.clear()
print(nombres)

#borrar la lista por completo
del nombres
print(nombres)