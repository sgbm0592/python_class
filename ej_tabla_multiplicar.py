import random

numero = random.randint(1, 10)

for val in range(11):
    print('{} x {} = {} '.format(numero, val, val*numero))
