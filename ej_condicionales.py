a = type(True)
b = type(False)

print(a == b)

#Ejemplo 1
billetera = 100
agua = 100
compra_exitosa = billetera >= agua
print(compra_exitosa)

#Ejemplo 2
billetera = 100
agua = 100
compra_exitosa = billetera > agua
print(compra_exitosa)

#Ejemplo teorico

num_a = 3
num_b = 5

print(num_a == num_b)
print(num_a != num_b)
print(num_a > num_b)
print(num_a >= num_b)
print(num_a < num_b)
print(num_a <= num_b)
print(num_a is num_b)
print(num_a is not num_b)

var_a = 2
var_b = 2
print('******objeto de memoria')
print(var_a is var_b)

