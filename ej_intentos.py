import random

numero = random.randint(0, 10)
print(numero)
valor = int(input('Ingresa un numero: '))

intentos = 1

while numero != valor:
    valor = int(input('Ingresa un numero: '))
    intentos += 1


print('intentos = {}'.format(intentos))