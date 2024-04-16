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