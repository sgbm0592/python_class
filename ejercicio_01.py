''' 
    1303
    Ejercicio 1

    Construir un Script que permita generar una fila de 'Sudoku', es decir, una fila de 9 valores
    con numeros del 1 al 9 y que ninguno de los valores se repitan y mostrar la fila.

    Para comprobar que la fila esta bien construida, deberan calcular la sumatoria de la fila y debe dar como resultado 45

    Al igual que en Sudoku, la fila se segmenta en 3 partes, por lo que es necesario calcular la sumatoria de cada bloque
    , mostrarlos e indicar que bloque es el mayor (A, B o C). en el caso de que existen bloque con igual valor, debera mostrar
    cuales son los bloques mayores. Y si todos son iguales, indicar el siguiente mensaje
    'Todos los bloques son iguales'.

    * Este script se puede resolver con las funciones y metodos vistas en clase, no es necesario implementar algo fuera de la misma
    y en el caso de realizarlo, debera escribir un comentario de la justificacion.

    * El objetivo de este ejercicio es evaluar los conocimientos adquiridos, como a su vez las buenas practicas y la optimizacion
    de la solucion, por lo que todos estos factores seran considerados para su evaluacion.

'''

import random

fila_sudoku = []
sumatoria = 0
bloque_a = 0
bloque_b = 0
bloque_c = 0
index = 0

while index < 9:
    numero = random.randint(1, 9)

    if not (numero in fila_sudoku):
        fila_sudoku.append(numero)
        sumatoria = sumatoria + numero

        if index <= 2:
            bloque_a += numero
        elif index <= 5:
            bloque_b += numero
        else:
            bloque_c += numero

        index += 1

print('Fila Sudoku = {}'.format(fila_sudoku))
print('Sumatoria = {}'.format(sumatoria))
print('Bloque A = {}'.format(bloque_a))
print('Bloque B = {}'.format(bloque_b))
print('Bloque C = {}'.format(bloque_c))

if bloque_a == bloque_b and bloque_a == bloque_c:
    print('Todos los bloques son iguales.')
elif bloque_a == bloque_b and bloque_c < bloque_a:
    print('Bloque A y B son mayores.')
elif bloque_c == bloque_b and bloque_a < bloque_c:
    print('Bloque C y B son mayores.')
elif bloque_a == bloque_c and bloque_b < bloque_a:
    print('Bloque A y C son mayores.')
elif bloque_b < bloque_a and bloque_c < bloque_a:
    print('Bloque A es mayor')
elif bloque_a < bloque_b and bloque_c < bloque_b:
    print('Bloque B es mayor')
elif bloque_a < bloque_c and bloque_b < bloque_c:
    print('Bloque C es mayor')