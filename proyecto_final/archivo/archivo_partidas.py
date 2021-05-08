import json
import random
from proyecto_final.partida.partida import Partida
from proyecto_final.jugador.jugador import Jugador

__partidas_archivo='partidas.json'
__partidas_archivos=('partida_1.json', 'partida_2.json', 'partida_3.json')


datos = {
    'partidas': []
}
partidas = datos['partidas']


def get_random_list(max):
    min = 0
    lista = random.sample(range(min, max), max)
    return lista


def crear_partidas(jugadores):
    total_jugadores = len(jugadores)
    total_partidas = int(total_jugadores/2)
    partidas = []
    lista = get_random_list(total_jugadores)
    i = 0
    j = 1
    while len(partidas) < total_partidas:
        partidas.append(Partida(numero=j, jugador_1=jugadores[lista[i]], jugador_2=jugadores[lista[i+1]]))
        i += 2
        j += 1
    return partidas


def get_finalistas(partidas):
    ultima_partida = partidas[-1]
    finalistas = []
    for partida in ultima_partida:
        jugador_1 = partida.get_jugador_1()
        jugador_2 = partida.get_jugador_2()
        if jugador_1.get_puntos() > jugador_2.get_puntos():
            finalistas.append(jugador_1)
        elif jugador_2.get_puntos() > jugador_1.get_puntos():
            finalistas.append(jugador_2)
        else:
            finalistas.append(jugador_1)
            finalistas.append(jugador_2)

    return finalistas



def export_partidas(partidas):
    nombre = 'partida_{}'.format(get_numero_partia(partidas))
    nombre_archivo = '{}.json'.format(nombre)
    dict_partidas = __partidas_to_dict(partidas,)
    with open(nombre_archivo, 'w') as archivo:
        json.dump(dict_partidas, archivo)


def get_numero_partia(partidas):
    if len(partidas) == 4:
        return 1
    elif len(partidas) == 2:
        return 2
    elif len(partidas) == 1:
        return 3


def existe_archivo(nombre_archivo):
    from pathlib import Path

    archivo = Path(nombre_archivo)
    return archivo.is_file()

def get_partidas():
    partidas = []
    try:
        for archivo in __partidas_archivos:
            partida = []
            if existe_archivo(archivo):
                with open(archivo, 'r') as archivo_lectura:
                    data = json.load(archivo_lectura)

                for jugada in data['partidas']:
                    partida.append(Partida(jugada['numero'],
                                        Jugador(jugada['jugador_1']['nombre'], jugada['jugador_1']['email'],
                                                jugada['jugador_1']['raza'], jugada['jugador_1']['puntos']),
                                        Jugador(jugada['jugador_2']['nombre'], jugada['jugador_2']['email'],
                                                jugada['jugador_2']['raza'], jugada['jugador_2']['puntos'])
                                            ))

                partidas.append(partida)
    except Exception as e:
        print('No existen partidas, se crearan nuevas partidas')

    return partidas


def get_jugador_data(jugador):
    return {'nombre': jugador.get_nombre(), 'email': jugador.get_email(),
            'raza': jugador.get_raza(), 'puntos': jugador.get_puntos()}


def __partidas_to_dict(partidas):
    dict_partidas = {}
    lista_jugada = []
    for jugada in partidas:
        jugador_1 =jugada.get_jugador_1()
        jugador_2 = jugada.get_jugador_2()
        lista_jugada.append({'numero': jugada.get_numero(),
                            'jugador_1':get_jugador_data(jugador_1),
                             'jugador_2': get_jugador_data(jugador_2)
                             })
    dict_partidas['partidas'] = lista_jugada

    return dict_partidas



