''' 
    1303
    Ejercicio 2

    Construir un Script que dado un archivo de texto, que al leerse y procesarce se obtiene una variable data 
    que contiene la cantidad de jugadores de StarCraft por ciudad de Argentina.
    (ver variable data)

    Se solicita:
    # Calcular el total de jugadores existentes en la Argentina
    # Cual o cuales es/son la/s provincia/s con mayor cantidad de jugadores
    # Conociendo que el pais se divide en tres zonas, calcule la cantidad de jugadores por zona:
        # Norte = Formosa, Salta, Tucuman, La Rioja, Santa Fe
        # Centro = CABA, Buenos Aires, Mendoza, Cordoba
        # Sur = Chubut, Tierra del Fuego, Rio Negro

    Una vez realizado este requerimiento es necesario agregar a la lista el siguiente registro :
        # Rio Negro
        # 4 Jugadores

    Despues de agregar el elemento se requiere:
        # Calcular el total de jugadores existentes en la Argentina
        # Cual o cuales es/son la/s provincia/s con menor cantidad de jugadores
        # Cual es la region con mayor cantidad de jugadores.

    * Este script se puede resolver con las funciones y metodos vistas en clase, no es necesario implementar algo fuera de la misma
    y en el caso de realizarlo, debera escribir un comentario de la justificacion.

    * El objetivo de este ejercicio es evaluar los conocimientos adquiridos, como a su vez las buenas practicas y la optimizacion
    de la solucion, por lo que todos estos factores seran considerados para su evaluacion.
'''

data = [
    ['CABA','Buenos Aires','Formosa','Salta','Tucuman','La Rioja','Cordoba','Mendoza','Chubut','Tierra del Fuego','Santa Fe'],
    ['45','40','0','1','2','1','45','10','1','0','200']
]

total_jugadores = 0
index = 0
mayor = 0
norte = 0
centro = 0
sur = 0
index_mayores = []
while index < len(data[1]):
    jugadores = int(data[1][index])
    total_jugadores = total_jugadores + jugadores

    if jugadores >= mayor:
        mayor = jugadores
        index_mayor = index
        index_mayores.append(index)

    provincia = data[0][index]
    if provincia in ('Formosa', 'Salta', 'Tucuman', 'La Rioja', 'Santa Fe'):
        norte = norte + jugadores
    elif provincia in ('CABA', 'Buenos Aires', 'Mendoza', 'Cordoba') :
        centro = centro + jugadores
    elif provincia in ('Chubut', 'Tierra del Fuego', 'Rio Negro'):
        sur = sur + jugadores
    index += 1

print(data)
print(index_mayor)

# Calcular el total de jugadores existentes en la Argentina
print('Total de Jugadores = {}'.format(total_jugadores))
# Cual o cuales es/son la/s provincia/s con mayor cantidad de jugadores
print('Provincia con mayor Jugadores = {} - {}'.format(data[0][index_mayor], mayor))
# Conociendo que el pais se divide en tres zonas, calcule la cantidad de jugadores por zona:
        # Norte = Formosa, Salta, Tucuman, La Rioja, Santa Fe
        # Centro = CABA, Buenos Aires, Mendoza, Cordoba
        # Sur = Chubut, Tierra del Fuego, Rio Negro
print('Jugadores por Zona \n\t Norte = {} \n\t Centro = {} \n\t Sur = {}'.format(norte, centro, sur))


for index in index_mayores:
    print('Provincia con mayor Jugadores = {} - {}'.format(data[0][index], data[1][index]))

data[0].append('Rio Negro')
data[1].append(4)
menor = 0
total_jugadores = total_jugadores + data[1][-1]

provincia = data[0][-1]
if provincia in ('Formosa', 'Salta', 'Tucuman', 'La Rioja', 'Santa Fe'):
    norte = norte + jugadores
elif provincia in ('CABA', 'Buenos Aires', 'Mendoza', 'Cordoba'):
    centro = centro + jugadores
elif provincia in ('Chubut', 'Tierra del Fuego', 'Rio Negro'):
    sur = sur + jugadores

index = 0
index_menores = []
while index < len(data[1]):
    jugadores = int(data[1][index])
    if jugadores <= menor:
        menor = jugadores
        index_menor = index
        index_menores.append(index)
    index += 1

#Despues de agregar el elemento se requiere:
print('\n')
# Calcular el total de jugadores existentes en la Argentina
print('Total de Jugadores = {}'.format(total_jugadores))
# Cual o cuales es/son la/s provincia/s con menor cantidad de jugadores
print('Provincia con menor cantidad de Jugadores = {} - {}'.format(data[0][index_menor], menor))
# Cual es la region con mayor cantidad de jugadores.
print('Jugadores por Zona \n\t Norte = {} \n\t Centro = {} \n\t Sur = {}'.format(norte, centro, sur))

for index in index_menores:
    print('Provincia con menor Jugadores = {} - {}'.format(data[0][index], data[1][index]))