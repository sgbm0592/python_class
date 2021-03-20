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
nuevo_contacto = {}

while opcion != 0:
    print('\n\n\nMenu:\n\t1 Agregar Contacto\n\t2 Ver Contactos\n\t3 Buscar Contacto\n\t4 Eliminar Contacto\n\t0 Salir')
    opcion = int(input('Elige una opcion: '))

    if opcion == 1:
        nuevo_contacto['nombre'] = str(input('Ingresa un nombre: '))
        nuevo_contacto['numero'] = str(input('Ingresa un numero de telefono: '))
        nuevo_contacto['email'] = str(input('Ingresa un email: '))
        contactos.append(nuevo_contacto)
        print('Contacto agregado.')

    elif opcion == 2:
        for contacto in contactos:
            print('\n ******* Contactos *******')
            for key, value in contacto.items():
                print('\t{} - {}'.format(key, value))

    elif opcion == 3:
        print('Buscar Contacto')
        nombre = str(input('Ingresa un nombre: '))
        indice = 0
        nombre_agenda = ''
        encontrado = False

        while indice < len(contactos) or nombre != nombre_agenda:
            nombre_agenda = contactos[indice].get('nombre')
            if nombre == nombre_agenda:
                contacto = contactos[indice]
                encontrado = True
                print('Los datos son:')
                print('\n\t {} - {} - {}'.format(contacto.get('nombre'),
                                                 contacto.get('numero'),
                                                 contacto.get('email')))

            indice += 1

        if not encontrado:
            print('El contacto {} no se encuentra en en la agenda'.format(nombre))
    elif opcion == 4:
        print('Eliminar Contacto')
        nombre = str(input('Ingresa un nombre: '))
        indice = 0
        encontrado = False

        for contacto in contactos:
            if contacto['nombre'] == nombre:
                contacto = contactos[indice]
                encontrado = True
                contactos.pop(indice)
                print('Contacto eliminado correctamente:')

        if not encontrado:
            print('El contacto {} no se encuentra en en la agenda'.format(nombre))

    elif opcion == 0:
        break
    else:
        print('No es una opcion valida.')



