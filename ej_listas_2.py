import random

numeros = []

for x in range(1, 10):
    numero = random.randint(1, 9)
    numeros.append(numero)

print('numeros = {}'.format(numeros))

count = 0

repetidos = False

while count < len(numeros)-1:
    temp = numeros[count]
    numeros.pop(count)
    if temp in numeros:
        repetidos = True
        print('{} esta repetido'.format(temp))
        break

    count += 1

if not repetidos:
    print('No hay repetidos')