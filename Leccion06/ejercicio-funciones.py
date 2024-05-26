"""
Crear una función para sumar los valores recibidos de tipo numérocp,
utilizando argumentos variables *args como parámetro de la función
y regresar como resultado la suma de todos los valores pasados como argumentos.
"""

# definimos nuestra funcion para sumar valores
def sumar_valores(*args):
    resultado = 0
    # Iteramos cada elemento 
    for valor in args:
        # resultado = resultado + valor
        resultado += valor
    return resultado 

# llamada a la función
print(sumar_valores(3,5,9))
