import random

numero = random.randint(1, 10)
print(numero)

for i in range(1, numero+1):
    print('{}'.format(i*'*'))