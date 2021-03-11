"""for num in range(1, 99):
    if num == valor:
        break
    print(num)
    res += num
print(res)"""

import random
numero = random.randint(1, 20)
print(numero)
numero *= 2

num = 2
result = 0
while num < 99 and num != numero:
    result += num
    num += 1

print(numero)
res = 0

valor = 4
num = 1
res = 1
while num < 99 and num != valor:
    print(num)
    res += num
    num += 1

print(res)
