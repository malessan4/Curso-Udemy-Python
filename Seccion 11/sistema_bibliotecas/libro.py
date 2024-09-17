class Libro:
    contador_libro = 0
    
    def __init__(self, titulo, autor, genero):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        Libro.contador_libro += 1
        self.id = Libro.contador_libro
        
    @classmethod
    def obtener_total_libros(cls):
        return cls.contador_libro
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def autor(self):
        return self._autor
    
    @property
    def genero(self):
        return self._genero