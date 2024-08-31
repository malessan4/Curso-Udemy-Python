class Aritmetica:
    
    def __init__(self, operando1=None, operando2=None):
        self._operando1 = operando1
        self._operando2 = operando2
        
    def sumar(self):
        resultado = self._operando1 + self._operando2
        print(f'Suma entre:  {self.operando1} + {self.operando2} = {resultado}')
    
    def restar(self):
        resultado = self._operando1 - self._operando2
        print(f'Restra entre: {self._operando1} - {self._operando2} = {resultado}')
        
    def multiplicar(self):
        resultado = self._operando1 - self._operando2
        print(f'Multiplicacion entre: {self._perando1} - {self._operando2} = {resultado}')
    
    def division (self):
        resultado = self._operando1 - self._operando2
        print(f'Division entre: {self._operando1} - {self._operando2} = {resultado}')

    @property
    def operando1(self):
        return self._operando1
    
    @operando1.setter
    def operando1(self, operando1):
        self._operando1 = operando1
    
    @property
    def operando2(self):
        return self._operando2
    
    @operando2.setter
    def operando2(self, operando2):
        self._operando2 = operando2
        
aritmetica1 = Aritmetica(5,7)
print(f'Valor operando1 del objeto aritmetica1: {aritmetica1.operando1}')
print(f'Valor operando1 del objeto aritmetica1: {aritmetica1.operando2}')
print()

aritmetica2 = Aritmetica(12,16)
print(f'Valor operando1 del objeto aritmetica1: {aritmetica2.operando1}')
print(f'Valor operando1 del objeto aritmetica1: {aritmetica2.operando2}')
print()
    
aritmetica2.sumar()
print()
aritmetica1.operando1 = 10
aritmetica1.operando2 = 500
aritmetica1.restar()