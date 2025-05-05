from monitor import Monitor
from Teclado import Teclado
from Raton import Raton

class Computadora:
    contador_computadoras = 0
    
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self.id_computadora = Computadora.contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton
        
    def __str__(self):
        return f'''{self.nombre}: ID: {self.id_computadora}
Monitor: {self.monitor}
Teclado: {self.teclado}
Raton: {self.raton}'''
        
if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('HP', '25')
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    print(computadora1)
    
    print()
    
    teclado2 = Teclado('Gamer', 'Bluetooth')
    raton2 = Raton('Gamer', 'Bluetooth')
    monitor2 = Monitor('Gamer', 34)
    computadora2 = Computadora('Gamer', monitor2, teclado2, raton2)
    print(computadora2)