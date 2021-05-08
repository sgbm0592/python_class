from proyecto_final.archivo.archivo_jugadores import get_jugadores, export_jugadores
from proyecto_final.archivo.archivo_partidas import crear_partidas, export_partidas, get_partidas, get_finalistas
from proyecto_final.jugador.jugador import Jugador

opcion = -1


def mostrar_menu():
    print('\n\nMenu:\n\t1) Crear Jugadores\n\t2) Ver Jugadores Inscritos'
          '\n\t3) Crear Partidas\n\t4) Elegir Ganadores'
          '\n\t5) Ver Jugadores por Ranking\n\t6) Histórico de Partidas realizadas'
          '\n\t0) Salir')

def elegir_raza():
    raza = None
    while not raza:
        opcion_raza = int(input('\t1)Terran 2)Zerg 3)Protoss \nElige una raza: '))
        if opcion_raza == 1:
            raza = 'Terran'
        elif opcion_raza == 2:
            raza = 'Zerg'
        elif opcion_raza == 3:
            raza = 'Protoss'
        else:
            print('No es una opcion valida.')

    return raza


def get_puntos_por_partidas(partidas):
    if len(partidas) == 4:
        return 1, 0
    elif len(partidas) == 2:
        return 3, 0
    elif len(partidas) == 1:
        return 5, 3


def crear_jugador():
    print('Agregar jugador')
    nombre = input('Ingresa un nombre: ')
    email = input('Ingresa un email: ')
    raza = elegir_raza()
    nuevo_jugador = Jugador(nombre, email, raza, 0)
    print('jugador agregado.')
    return nuevo_jugador


def crear_jugadores():
    print('\t Debes crear 8 jugadores para iniciar una partida')
    nuevos_jugadores = []
    for i in range(8):
        nuevo_jugador = crear_jugador()
        nuevos_jugadores.append(nuevo_jugador)
    export_jugadores(nuevos_jugadores)


def ver_jugadores_inscritos():
    lista_jugadores = get_jugadores()
    print('\n\t** Lista de Jugadores Inscritos **\n')
    for jugador in lista_jugadores:
        print('\t {}'.format(jugador))


def crear_nuevas_partidas():
    print('\t ***** Nuevas Partidas *****')
    partidas = get_partidas()
    jugadores = get_finalistas(partidas) if partidas else get_jugadores()
    nuevas_partidas = crear_partidas(jugadores)
    export_partidas(nuevas_partidas)
    for partida in get_partidas():
        print('\t {}'.format(partida))
    return nuevas_partidas


def eligir_ganadores(partidas):
    print('\t ***** Elegir Ganadores ?? *****')
    puntos_1, puntos_2 = get_puntos_por_partidas(partidas)
    jugadores = []
    for partida in partidas:
        jugador_1 = partida.get_jugador_1()
        jugador_2 = partida.get_jugador_2()

        print('\t {}'.format(partida))
        ganador = int(input('Quien es el Ganador de la Partida {}  1) {} 2) {} ? '.format(partida.get_numero(),
                                                                          jugador_1.get_nombre(),
                                                                          jugador_2.get_nombre())))
        if ganador == 1:
            jugador_1.set_puntos(jugador_1.get_puntos() + puntos_1)
            jugador_2.set_puntos(jugador_2.get_puntos() + puntos_2)
        elif ganador == 2:
            jugador_2.set_puntos(jugador_2.get_puntos() + puntos_1)
            jugador_1.set_puntos(jugador_1.get_puntos() + puntos_2)
        else:
            print('No es una opcion correcta')

        jugadores.append(jugador_1)
        jugadores.append(jugador_2)
    export_jugadores(jugadores)
    export_partidas(partidas)

def get_ranking_jugadores(todas_partidas):
    jugadores = {}
    for partidas in todas_partidas:
        for partida in partidas:
            jugador_1 = partida.get_jugador_1()
            jugador_2 = partida.get_jugador_2()
            jugadores[jugador_1.get_nombre()] = jugador_1.get_puntos()
            jugadores[jugador_2.get_nombre()] = jugador_2.get_puntos()
    return jugadores

def get_ganador(jugador_1, jugador_2):
    if jugador_1.get_puntos() > jugador_2.get_puntos():
        return jugador_1
    return jugador_2

def ver_historicos_partidas(todas_partidas):
    i = 1
    jugadores = {}
    for partidas in todas_partidas:
        print('\t\tPartida #{}'.format(i))
        for partida in partidas:
            jugador_1 = partida.get_jugador_1()
            jugador_2 = partida.get_jugador_2()
            ganador = get_ganador(jugador_1, jugador_2)
            print('{} - {} - Ganador --> {}'.format(jugador_1.get_nombre(), jugador_2.get_nombre(), ganador.get_nombre()))
        i+=1

partidas = None
partidas = get_partidas()

while opcion != 0:
    mostrar_menu()
    opcion = int(input('Elige una opcion: '))

    if opcion == 1:
        crear_jugadores()
    elif opcion == 2:
        ver_jugadores_inscritos()
    elif opcion == 3:
        partidas = crear_nuevas_partidas()
    elif opcion == 4:
        if partidas:
            eligir_ganadores(partidas)
            partidas = None
        else:
            print('Elige la opcion 3) Crear partidas para comenzar.')
    elif opcion == 5:
        print('Ver Jugadores por Ranking')
        ranking = get_ranking_jugadores(partidas)
        print(sorted(ranking.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))
    elif opcion == 6:
        print('Histórico de Partidas realizadas')
        ver_historicos_partidas(partidas)
    elif opcion == 0:
        break
    else:
        print('No invalida')