from DispositivoEntrada.py import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0
    
    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
        self.marca = marca
        self.tipo_entrada = tipo_entrada
        
    