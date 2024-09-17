class Animal:
    def comer(self):
        print('Como muchas veces al dia')
        
    def dormir(self):
        print('Duermo muchas horas')
        
class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')
        
        
# Programa principal
print('*** Ejemplo de Herencia en Python ***')
print('Clase Padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()