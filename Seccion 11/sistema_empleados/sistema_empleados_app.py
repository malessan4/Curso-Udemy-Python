from empresa import Empresa
from empleado import Empleado

print('*** Sistema de Empleados ***')

# Crear una instancia de una empresa
empresa1 = Empresa('Global Mentoring')

# Contratar algunos empleados
empresa1.contratar_empleado('Juan', 'Ventas')
empresa1.contratar_empleado('Maria', 'Marketing')
empresa1.contratar_empleado('Pedro', 'Ventas')
empresa1.contratar_empleado('Ana', 'Recursos Humanos')

# Obtener el total de objetos de tipo empleado
print(f'Total de empleados: {Empleado.obtener_total_empleados()}')

# Obtener el numero de empleados en el departamento de ventas
print(f'Empleados en el departamento de Ventas: '
    f'{empresa1.obtener_numero_empleados_departamento('Ventas')}')

# Mostrar todos los empleados de la empresa 1
empresa1.obtener_total_empleados()