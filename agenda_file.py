nombre_archivo='agenda.txt'
archivo = open(nombre_archivo, 'w')

opcion = -1
archivo.write('nombre,numero,email\n')
archivo.write('Gaby,4339355831,gaby@turning.io\n')
archivo.write('Sandra,4921859545,sgbm0592@gmail.com\n')
archivo.write('Adolfo,3339802345,luna_adolfo@gmail.com\n')
archivo.write('Adolfo Rios,3339802345,luna_adolfo@gmail.com\n')
archivo.close()

while opcion != 0:
    print('\n\n\nMenu:\n\t1 Agregar Contacto\n\t2 Ver Contactos\n\t3 Buscar Contacto\n\t4 Eliminar Contacto\n\t0 Salir')
    opcion = int(input('Elige una opcion: '))

    if opcion == 1:
        archivo = open(nombre_archivo, 'w')
        nombre = str(input('Ingresa un nombre: '))
        numero = str(input('Ingresa un numero de telefono: '))
        email = str(input('Ingresa un email: '))
        archivo.write('{},{},{}'.format(nombre, numero, email))
        archivo.close()
        print('Contacto agregado.')

    elif opcion == 2:
        print('Ver Contactos')
        archivo = open('agenda.txt', 'r')
        contactos = archivo.readlines()
        for contacto in contactos:
            data = contacto.split(',')
            print('nombre:{} - numero:{} - email:{}'.format(data[0], data[1], data[2]))
        archivo.close()
    elif opcion == 3:
        archivo = open(nombre_archivo, 'r')
        print('Buscar Contacto')
        nombre = str(input('Ingresa un nombre: '))
        indice = 0
        nombre_agenda = ''
        encontrado = False

        contactos = archivo.readlines()
        for contacto in contactos:
            if nombre in contacto:
                print(contacto)
                encontrado=True
        archivo.close()

        if not encontrado:
            print('El contacto {} no se encuentra en en la agenda'.format(nombre))
    elif opcion == 4:
        archivo = open(nombre_archivo, 'r')
        print('Eliminar Contacto')
        nombre = str(input('Ingresa un nombre: '))
        indice = 0
        encontrado = False
        nuevos_contactos = []

        contactos = archivo.readlines()
        for contacto in contactos:
            if nombre in contacto:
                confirmar = int(input('Deseas eliminar a {}? 1)Si 0)No'.format(contacto.split(',')[0])))
                if confirmar == 0:
                    nuevos_contactos.append(contacto)
                encontrado = True
            else:
                nuevos_contactos.append(contacto)
        archivo.close()
        archivo = open(nombre_archivo, 'w')

        for contacto in nuevos_contactos:
            archivo.write(contacto)
        archivo.close()
        if not encontrado:
            print('El contacto {} no se encuentra en en la agenda'.format(nombre))

    elif opcion == 0:
        break
    else:
        print('No es una opcion valida.')



