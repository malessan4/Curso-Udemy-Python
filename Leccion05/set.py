#un set no mantiene un orden y tampoco permite almacenar elementos duplicados
#no es posible modificar los elementos almacenados al set
#pero si es posible agregar o eliminar elementos

planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
print(len(planetas))
print('Marte' in planetas)
planetas.add('Tierra')
print(planetas)
planetas.remove('Tierra')
print(planetas)
planetas.clear()
print(planetas)
del planetas
print(planetas)