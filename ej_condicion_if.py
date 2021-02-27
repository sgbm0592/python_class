import datetime

numero_mes = 6
if numero_mes > 12 or numero_mes < 0:
    print('No es un numero valido, elige de 1 a 12')

if numero_mes == 3 or numero_mes == 4 or numero_mes == 5:
    print('Primavera')
elif numero_mes == 6 or numero_mes == 7 or numero_mes == 8:
    print('Verano')
elif numero_mes == 9 or numero_mes == 10 or numero_mes == 11:
    print('Otoño')
else:
    print('Invierno')


"""mes = datetime.date(2021, numero_mes, 1).strftime('%b')
print(mes)

if mes in ('Mar', 'Apr', 'May'):
    print('Primavera')
elif mes in ('June', 'July', 'Aug'):
    print('Verano')
elif mes in ('Sept', 'Oct', 'Nov'):
    print('Otoño')
else:
    print('Invierno')"""