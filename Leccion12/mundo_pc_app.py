from monitor import Monitor
from Teclado import Teclado
from Raton import Raton
from computadora import Computadora
from Orden import Orden

print('***Mundo PC***')


teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP', '25')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('Gamer', 'Bluetooth')
raton2 = Raton('Gamer', 'Bluetooth')
monitor2 = Monitor('Gamer', 34)
computadora2 = Computadora('Gamer', monitor2, teclado2, raton2)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)


teclado3 = Teclado('Dell', 'USB')
raton3 = Raton('Dell', 'Bluetooth')
monitor3 = Monitor('Dell', 30)
computadora3 = Computadora('Dell', monitor3, teclado3, raton3)
orden1.agregar_computadora(computadora3)

print(orden1)