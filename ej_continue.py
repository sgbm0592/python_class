result = 0

for numero in range(1,10):
    if numero%2 == 0:
        continue
    result += numero

print(result)