nombre = 'Gaby'
apellido = 'Muro'
pais = 'Mexico'
edad = 28

#Ejemplo 1
print('Mi nombre completo es: {} {}'.format(nombre, apellido))
#Ejemplo 2
print(f'Mi nombre completo es: {nombre} {apellido}')

#Ejemplo 3
texto_a = 'Hola QA Minds, mi nombre es: %s, y soy de: %s y tengo %s años' %(nombre, pais, edad)
print(texto_a)

#Ejemplo 4
texto_b = 'Hola QA Minds, mi nombre es: '+nombre+' y soy de: '+ pais+' y tengo '+str(edad)+' años'
print(texto_b)