
lista_poker = [0, 0.5, 1, 2, 3, 5, 8, 13, 20, 40, 100]

pares = 0
sumatoria = 0
divisibles = 0

count = 0
while count < len(lista_poker):
    valor = lista_poker[count]
    if valor % 2 == 0:
        pares += 1

    if valor !=0 and type(valor) != float and valor % lista_poker[count-1] == 0:
        divisibles += 1

    count += 1
    sumatoria = valor + sumatoria

print('total de pares = {}'.format(pares))
print('total de divisibles = {}'.format(divisibles))
print('sumatoria = {}'.format(sumatoria))
