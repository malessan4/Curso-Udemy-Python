#Definimos la clase coche

class Coche:
    
    def __init__(self, marca, modelo, color):
        self._marca = marca # Atributo protegido
        self._modelo = modelo # Atributo protegido
        self._color = color # Atributo protegido
    
    def conducir(self):
        print(f'''Conduciendo el coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')
        
#    def get_marca(self):
#        return self._marca

    @property # definir el metodo get de manera más python
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def set_modelo(self, modelo):
        self._modelo = modelo

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color


coche1 = Coche('Toyota', 'Yaris', 'Azul')
coche1.conducir()
print()

#coche1.set_marca('Toyota 2')
#coche1.set_modelo('Yaris 2')
#coche1.set_color('Azul 3') 
coche1.conducir()
#Atributo de marca del coche 1
print(f'Atributo marca coche1: {coche1.marca}')
coche1.marca = 'Toyota 3'
print(f'Atributo marca coche1: {coche1.marca}')
coche1.fuerza_motor = '1.6' # le agrega otro atributo
print(f'Fuerza del motor {coche1.fuerza_motor}')
print(f'Atributos del coche1: {coche1.__dict__}')
print()

coche2 = Coche('Chevrolet', 'Corsa', 'Gris')
coche2.conducir()