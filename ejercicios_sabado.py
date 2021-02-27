a = 'hola'
A = 'Mundo'
a = 6
a = 7.1
a = False

print(a)
'''
    Este archivo se encarga de generar mediante la libreria de datetime
    la fecha del dia de hoy y la imprime en pantalla.
'''
from datetime import datetime, date

# obtiene el valor del dia de hoy
hoy = datetime.now().day
hoy_date = date.today().day
#Imprime el valor de hoy
print(hoy)
print(hoy_date)

