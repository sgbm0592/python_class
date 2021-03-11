number = 8
var_control = 0
resultado = 0

while var_control <= number:
    if var_control % 2 == 0:
        resultado += var_control
    var_control += 1

print('Sumatoria = {}'.format(resultado))