class Animal:
    def comer(self):
        print('Como muchas veces al dia')
        
    def dormir(self):
        print('Duermo muchas horas')

        
class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

# Sobreescribimos el metodo dormir()         
    def dormir(self):
        print('Duermo 8 horas')    
    
        
        
# Programa principal
print('*** Ejemplo de Herencia en Python ***')
print('Clase Padre, soy un Animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()


print('\nClase Hija, soy un perro')
perro1 = Perro()
perro1.hacer_sonido()
perro1.comer()
perro1.dormir()