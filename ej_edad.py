import datetime
mes = 6
dia = 5
year = 1992

fecha_nacimiento = datetime.date(year, mes, dia)
hoy = datetime.datetime.now()

years = hoy.year - fecha_nacimiento.year

print('Tienes {} years. \n'.format(years))

if fecha_nacimiento.month > hoy.month:
    print('Tu cumpleaños aún no ha pasado. \n')
else:
    print('Tu cumpleaños ya paso! \n')

if year >= 1920 and year <= 1939:
    print('Perteneces a la Generacion Silenciosa \n')
elif year >= 1940 and year <= 1959:
    print('Perteneces a los Baby Boomers \n')
elif year >= 1960 and year <= 1979:
    print('Perteneces a la Generacion X \n')
elif year >= 1980 and year <= 1989:
    print('Perteneces a la Generacion Y \n')
else:
    print('Perteneces a la Generacion Z \n')

