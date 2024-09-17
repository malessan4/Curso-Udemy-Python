from biblioteca import Biblioteca
from libro import Libro

bibliotecaNacional = Biblioteca('Biblioteca Nacional')
print(f'*** Bienvenidos a la {bibliotecaNacional.nombre} ***')

# Definicion de libros

libro1 = Libro('El señor de los anillos', 'JRR Tolkien', 'fantasia')
libro2 = Libro('Don Quijote de la Manca', 'Miguel de Cervantes', 'Sátira')
libro3 = Libro('El amor en los tiempos de colera', 'Gabriel Garcia Marquez', 'Novela realismo magico')
libro4 = Libro('Fundacion', 'Issac Asimov', 'ciencia ficcion')
libro5 = Libro('Fundacion e imperio', 'Issac Asimov', 'ciencia ficcion')
libro6 = Libro('Segunda Fundacion', 'Issac Asimov', 'ciencia ficcion')

# Agrego libros a la biblioteca
bibliotecaNacional.agregar_libro(libro1)
bibliotecaNacional.agregar_libro(libro2)
bibliotecaNacional.agregar_libro(libro3)
bibliotecaNacional.agregar_libro(libro4)
bibliotecaNacional.agregar_libro(libro5)
bibliotecaNacional.agregar_libro(libro6)

# Busqueda por autor
# autor = input("Que autor desea buscar") 'Issac Asimov'
autor = 'Issac asimov'
print(f'\nLibros de {autor}')
bibliotecaNacional.buscar_libros_por_autor(autor)

print('  ')
# Busqueda libros por genero
genero = 'ciencia ficcion'
print(f'Libros de {genero}')
bibliotecaNacional.buscar_libros_por_genero(genero)

# Mostrar todos los libros de la biblioteca
bibliotecaNacional.mostrar_todos_los_libros()