class Persona:
    # Atributo de clase
    contador_personas = 0

    def __init__(self, nombre, apellido):
        # incrementamos el valor del  atributo de clase
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido
        
    def mostrar_persona(self):
        print(f'Persona: {self.id}, {self.nombre}, {self.apellido}')
    
    @staticmethod
    def get_contador_personas_estatico():
        print('Metodo estático')
        return Persona.contador_personas
    
    @classmethod
    def get_contador_personas_clase(cls):
        print('Método de Clase')
        return cls.contador_personas
        
print ('*** Ejemplo Contador de objetos de tipo Persona ***')
persona1 = Persona('Gerardo', 'Perez')
persona1.mostrar_persona()

# segundo objeto
persona2 = Persona('Daniel', 'Alvarez')
persona2.mostrar_persona()

# imprimir el valor del contador de objetos de personas
print(f'Contador objetos Persona: {Persona.contador_personas}')
print(f'Contador objetos Persona (static): {Persona.get_contador_personas_estatico()}')
print(f'Contador objetos Persona (clase): {Persona.get_contador_personas_clase()}')