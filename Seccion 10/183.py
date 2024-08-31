"""
Ejercicio: Convertidor de Temperatura
Realizar dos funciones para convertir de
grados celsius a fahrenheit y viceversa.
"""

def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32)* 5/9


respuesta = int(input("Ingrese 1 para Celsius, Ingrese 2 para Fahrenheit, o cualquier otro numero para salir: "))

if respuesta == 1:
    grado_celsius = float(input("Ingrese grados Celsius: "))
    resultado_fahrenheit = celsius_fahrenheit(grado_celsius)
    print("Resultado en Fahrenheit: ", resultado_fahrenheit)
elif respuesta == 2:
    grado_fahrenheit = float(input("Ingrese grados Fahrenheit: "))
    resultado_celsius = fahrenheit_celsius(grado_fahrenheit)
    print(f"Resultado en Celsius:  {resultado_celsius}")
else:
    print("Gracias por usar Convertidor3000 ")
    

