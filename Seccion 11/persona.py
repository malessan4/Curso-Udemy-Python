class Persona:
    
    # Constructor
    def __init__(self, nombre, apellido):
        #Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido
    
    
    def mostrar_persona(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')   
        print(f'Dir. mem self: {id(self)}') 
        print(f'Dir. mem hex self: {hex(id(self))}') 
        
#Creamos el objeto        
if __name__ == '__main__':
    #Creacion de un primer objeto
    persona1 = Persona('Layla', 'Acosta')
    persona1.mostrar_persona()
    print(f'Dir. mem self: {id(persona1)}') 
    
    
    #Creamos un segundo objeto
    persona2 = Persona('Ian', 'Sanchez')
    persona2.mostrar_persona()
    print(f'Dir. mem self: {id(persona2)}') 