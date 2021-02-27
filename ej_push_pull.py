edad = 15
altura = 1.61

if edad >= 14 and altura >= 1.62:
    res = 'puedes subirte a la montaña rusa'
elif edad < 14 and altura < 1.62:
    res = 'No puedes subirte por que no cumples con edad y altura'
elif edad < 14:
    res = 'No puedes subirte por que no cumples con edad '
else:
    res = 'No puedes subirte por que no cumples con  altura'

print(res)

altura_permitida = 1.62
edad_permitida = 14

if edad >= edad_permitida and altura >= altura_permitida:
    res = 'puedes subirte a la montaña rusa'
elif edad < edad_permitida and altura < altura_permitida:
    res = 'No puedes subirte por que no cumples con edad y altura'
elif edad < edad_permitida:
    res = 'No puedes subirte por que no cumples con edad '
else:
    res = 'No puedes subirte por que no cumples con  altura'

print(res)


