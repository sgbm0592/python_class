import datetime
mes = 6
dia = 5
año = 1992

fecha_nacimiento = datetime.date(año, mes, dia)
hoy = datetime.datetime.now()

años = hoy.year - año

print('Tienes {} años'.format(años))

if fecha_nacimiento.month > hoy.month:
    print('Tu cumpleaños aun no ha pasado')
else:
    print('Tu cumpleaños ya paso')

print('Tienes {} años'.format(años))
