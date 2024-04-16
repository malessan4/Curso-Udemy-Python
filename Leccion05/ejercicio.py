# sintaxis de range (inicio<opcional>, fin<requerido>, incremento<opcional>)

# ejercicio 1. Iterar un rango de 0 a 10 e imprimir números divisibles entre 3

# ejercicio 2. Crear un rango de numeros de 2 a 6, e imprimirlos

# ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1

# ejercicio 1.
print('Rango de 0 a 10 con numeros divisibles entre 3')
for i in range(11):
    if i % 3 !=0:
        continue
    print(f'Valor: {i}')
    
# ejercicio 2.
print('Rango con valores de inicio = 2 y fin = 6')
rango = range(2,7)
for i in rango:
    print(i)


# ejercicio 3.
print('Rango con valores de inicio = 3, fin = 10, incremento = 2')
rango = range (3,11,2)
#el numero 2 es el incremento
for i in rango:
    print(i)