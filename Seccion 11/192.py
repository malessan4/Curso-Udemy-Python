class Aritmetica:
    
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2
        
    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f'Suma entre:  {self.operando1} + {self.operando2} = {resultado}')
    
    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f'Restra entre: {self.operando1} - {self.operando2} = {resultado}')
        
    def multiplicar(self):
        resultado = self.operando1 - self.operando2
        print(f'Multiplicacion entre: {self.operando1} - {self.operando2} = {resultado}')
    
    def division (self):
        resultado = self.operando1 - self.operando2
        print(f'Division entre: {self.operando1} - {self.operando2} = {resultado}')

aritmetica1 = Aritmetica (2, 4)
aritmetica1.sumar()
aritmetica1.restar()
print()

aritmetica2 = Aritmetica (12, 16)
aritmetica2.sumar()
aritmetica2.multiplicar()
aritmetica2.division()