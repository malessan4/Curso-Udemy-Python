
vacaciones = False
diaDescanco = True
"""
if vacaciones or diaDescanco:
    print('Puede asistir al juego')
else:
    print('No se puede asistir')
"""

if not(vacaciones or diaDescanco):
    print('Tiene deber por hacer')
else:
    print('Puede asistir al juego')