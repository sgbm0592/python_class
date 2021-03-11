import random

lista = [1, 2, 3, 4, 5]

print('len = {}'.format(len(lista)))

numero = random.randint(1, 10)
print('numero = {}\n'.format(numero))


if numero not in lista:
    lista.pop(0)
else:
    position = 0
    for nums in lista:

        if numero == nums:
            lista.pop(position)

        position += 1

lista.append(numero)
print(lista)

print('len = {}'.format(len(lista)))
