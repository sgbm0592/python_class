numero_a = 9
numero_b = 3

var_control = 0
numeros = ''

numero_b += 1
while numero_b < numero_a:
    #numero_b += 1
    numeros += '{}, '.format(numero_b)
    numero_b += 1

print('los numeros son = {}'.format(numeros))
