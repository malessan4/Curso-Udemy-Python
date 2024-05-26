#esto lo va a tomar como una tupla
#args = argumentos
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)
        
listarNombres('Juan', 'Carla', 'Maria', 'Ernesto')
listarNombres('Laura', 'Carlos')