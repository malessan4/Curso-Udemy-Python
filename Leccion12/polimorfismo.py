class Animal:
    def comer(self):
        print('Como muchas veces al dia')
        
    def dormir(self):
        print('Duermo muchas horas')
        
    def hacer_sonido(self):
        print('Ruido Animal')

        
class Perro(Animal):
    def hacer_sonido(self):
        print('Guaf guaf')

# Sobreescribimos el metodo dormir()         
    def dormir(self):
        print('Duermo 8 horas')    
    
    
class Gato(Animal):
    def hacer_sonido(self):
        print('Miau miau')        
        
# Programa principal
print('*** Ejemplo de Herencia en Python ***')
print('Clase Padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()
animal1.hacer_sonido()


print('\nClase Hija, soy un perro')
perro1 = Perro()
perro1.hacer_sonido()
perro1.comer()
perro1.dormir()

print('\nClase Hija, soy un gato')
gato1 = Gato()
gato1.hacer_sonido()
gato1.comer()
gato1.dormir()