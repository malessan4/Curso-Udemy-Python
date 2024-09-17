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
        
    def dormir(self):
        print('Duermo 15 horas')          
        
def hacer_sonido_animal(animal):
    animal.hacer_sonido()

    
# Programa principal
print('*** Ejemplo de Herencia en Python ***')
print('Clase Padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()
hacer_sonido_animal(animal1)


print('\nClase Hija, soy un perro')
perro1 = Perro()
hacer_sonido_animal(perro1)
perro1.comer()
perro1.dormir()

print('\nClase Hija, soy un gato')
gato1 = Gato()
hacer_sonido_animal(gato1)
gato1.comer()
gato1.dormir()