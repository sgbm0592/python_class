import json
nombre_archivo='agenda.json'
archivo = open(nombre_archivo, 'w')

agenda = {
    'contactos' : []
}

opcion = -1
contactos = agenda['contactos']
nuevo_contacto = {'nombre': 'Gaby', 'numero': '4339355831', 'email': 'gaby@turning.io'}
contactos.append(nuevo_contacto)
nuevo_contacto = {'nombre': 'Sandra', 'numero': '4921859545', 'email': 'sgbm0592@gmail.com'}
contactos.append(nuevo_contacto)
nuevo_contacto = {'nombre': 'Adolfo', 'numero': '3339802345', 'email': 'luna_adolfo@gmail.com'}
contactos.append(nuevo_contacto)

with open(nombre_archivo, 'w') as archivo:
    json.dump(agenda, archivo)


while opcion != 0:
    if opcion in (1, 2, 3, 4):
        with open(nombre_archivo, 'r') as archivo_lectura:
            data = json.load(archivo_lectura)
            contactos_lista = data['contactos']

    print('\n\nMenu:\n\t1 Agregar Contacto\n\t2 Ver Contactos\n\t3 Buscar Contacto\n\t4 Eliminar Contacto\n\t0 Salir')
    opcion = int(input('Elige una opcion: '))

    if opcion == 1:
        nombre = input('Ingresa un nombre: ')
        numero = input('Ingresa un numero de telefono: ')
        email = input('Ingresa un email: ')
        nuevo_contacto = {'nombre': nombre, 'numero': numero, 'email': email}
        contactos_lista.append(nuevo_contacto)
        data['contactos'] = contactos_lista
        with open(nombre_archivo, 'w') as archivo_agregar:
            json.dump(data, archivo_agregar)
        print('Contacto agregado.')
    elif opcion == 2:
        print('Ver Contactos')
        for contacto in contactos_lista:
            print(contacto)
    elif opcion == 3:
        print('Buscar Contacto')
        nombre = input('Ingresa un nombre: ')
        indice = 0
        nombre_agenda = ''
        encontrado = False

        for contacto in contactos_lista:
            if nombre in contacto.values():
                print(contacto)#print('nombre:{} - numero:{} - email:{}'.format(data[0], data[1], data[2]))
                encontrado=True

        if not encontrado:
            print('El contacto {} no se encuentra en en la agenda'.format(nombre))
    elif opcion == 4:
        print('Eliminar Contacto')
        nombre = input('Ingresa un nombre: ')
        indice = 0
        encontrado = False
        nuevos_contactos = []

        for contacto in contactos_lista:
            if nombre in contacto.values():
                confirmar = int(input('Deseas eliminar a {}? 1)Si 0)No '.format(contacto)))
                if confirmar == 0:
                    nuevos_contactos.append(contacto)
                encontrado = True
            else:
                nuevos_contactos.append(contacto)

        data['contactos'] = nuevos_contactos
        with open(nombre_archivo, 'w') as archivo_eliminar:
            json.dump(data, archivo_eliminar)

        if not encontrado:
            print('El contacto {} no se encuentra en en la agenda'.format(nombre))
    elif opcion == 0:
        break
    else:
        print('No invalida')


