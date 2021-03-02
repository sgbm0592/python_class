import datetime
mes = 6
dia = 5
año = 1992

fecha_nacimiento = datetime.date(año, mes, dia)
hoy = datetime.datetime.now()

años = hoy.year - año

print('Tienes {} años. \n'.format(años))

if fecha_nacimiento.month > hoy.month:
    print('Tu cumpleaños aún no ha pasado. \n')
else:
    print('Tu cumpleaños ya paso! \n')

if año >= 1920 and año <= 1939:
    print('Perteneces a la Generacion Silenciosa \n')
elif año >= 1940 and año <= 1959:
    print('Perteneces a los Baby Boomers \n')
elif año >= 1960 and año <= 1979:
    print('Perteneces a la Generacion X \n')
elif año >= 1980 and año <= 1989:
    print('Perteneces a la Generacion Y \n')
elif año > 1990:
    print('Perteneces a la Generacion Z \n')

