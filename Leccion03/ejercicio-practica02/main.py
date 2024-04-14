calificacion = int(input('Ingrese el valor de la calificacion entre 0 y 10: '))
# if calificiacion >= 9 and calificacion <= 10 ------- anotacion clasica
if 9 <= calificacion <= 10: #anotacion simplificada
    print('A')
elif 8 <= calificacion < 9:
    print('B')
elif 7 <= calificacion < 8:
    print('C')
elif 6 <= calificacion < 7:
    print('D')
elif 0 <= calificacion < 6:
    print('F')
else:
    print('valor incorrecto de calificacion') 

    