from poo.archivo.archivo_tareas import get_tareas, export_tareas
from poo.archivo.archivo_usuarios import get_usuarios, export_usuarios
from poo.tarea.tarea import Tarea
from poo.usuario.usuario import Usuario

opcion = -1

def mostrar_menu():
    print('\n\nMenu:\n\t1) Agregar Usuario\n\t2) Agregar Tarea\n\t3) Buscar Tarea\n\t4) Ver Tareas\n\t'
          '5) Exportar Tareas\n\t6) Exportar Usuarios\n\t0 Salir')


def crear_usuario():
    print('Agregar Usuario')
    lista_usuarios = get_usuarios()
    nombre = input('Ingresa un nombre: ')
    email = input('Ingresa un email: ')
    nuevo_usuario = Usuario(nombre, email)
    lista_usuarios.append(nuevo_usuario)
    export_usuarios(lista_usuarios)
    print('Usuario agregado.')
    return nuevo_usuario


def buscar_usuario_por_email(email):
    lista_usuarios = get_usuarios()
    for usuario in lista_usuarios:
        if usuario.get_email() == email:
            return usuario
    opcion = int(input('El usuario no existe, Deseas crearlo? 1) Si 2)No'))

    if opcion == 1:
        nuevo_usuario = crear_usuario()
        return nuevo_usuario


def crear_tarea():
    print('Agregar Tarea')

    titulo = input('Ingresa un titulo: ')
    descripcion = input('Ingresa la descripcion: ')
    prioridad = input('Ingresa la prioridad: ')
    email = input('Ingresa el email del usuario a asignar')
    usuario = buscar_usuario_por_email(email)
    if not usuario:
        print('No se encontro un usuario')
        return
    nueva_tarea = Tarea(titulo, descripcion, prioridad, usuario)
    lista_tareas = get_tareas()
    lista_tareas.append(nueva_tarea)
    export_tareas(lista_tareas)
    print('Usuario agregado.')


def buscar_tarea(lista_tareas):
    print('Buscar Tarea')
    titulo = input('Ingresa un titulo: ')
    encontrado = False

    for tarea in lista_tareas :
        if titulo in tarea.get_titulo():
            print(tarea)
            encontrado = True

    if not encontrado:
        print('No se encontro la tarea {}.'.format(titulo))

def ver_tareas(lista_tareas):
    print('Ver Tareas')
    print('\n\nMenu:\n\t1 Todas\n\t2 Por Estado')
    opcion = int(input('Elige una opcion: '))

    if opcion == 1:
        print('Todas las tareas')
        for tarea in lista_tareas:
            print(tarea)
    elif opcion == 2:
        encontrado = False
        estado = str(input('Cual estado deseas buscar?: '))
        for tarea in lista_tareas:
            if estado in tarea.get_estado():
                print(tarea)
                encontrado = True

        if not encontrado:
            print('No se encontraron tareas en estado {}'.format(estado))

while opcion != 0:
    mostrar_menu()
    opcion = int(input('Elige una opcion: '))

    if opcion in (3, 4):
        lista_tareas = get_tareas()
    if opcion == 1:
        crear_usuario()
    elif opcion == 2:
        crear_tarea()
    elif opcion == 3:
        buscar_tarea(lista_tareas)
    elif opcion == 4:
        ver_tareas(lista_tareas)
    elif opcion == 5:
        print('Exportar Tareas')
        export_tareas(lista_tareas)
    elif opcion == 6:
        print('Exportar Usuarios')
        lista_usuarios = get_usuarios()
        export_usuarios(lista_usuarios)
    elif opcion == 0:
        break
    else:
        print('No invalida')


