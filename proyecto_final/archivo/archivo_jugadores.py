import json
from proyecto_final.jugador.jugador import Jugador

__jugadores_archivo='jugadores.json'


datos = {
    'jugadores': []
}
jugadores = datos['jugadores']
nueva_usuario = Jugador('Gaby', 'sgbm0592@gmail.com', 'Terran', 0)
jugadores.append(nueva_usuario)
nueva_usuario = Jugador('Adolfo', 'adolfo@gmail.com', 'Protoss', 0)
jugadores.append(nueva_usuario)
nueva_usuario = Jugador('Juan', 'juan@mail.com', 'Zerg', 0)
jugadores.append(nueva_usuario)
nueva_usuario = Jugador('Janneth', 'Janneth@hotmail.com', 'Terran',0)
jugadores.append(nueva_usuario)
nueva_usuario = Jugador('Ronnie', 'Ronnie@icloud.com', 'Protoss', 0)
jugadores.append(nueva_usuario)
nueva_usuario = Jugador('Octavio', 'Octavio@mail.com', 'Zerg', 0)
jugadores.append(nueva_usuario)
nueva_usuario = Jugador('Jime', 'compliance@turning.io', 'Protoss', 0)
jugadores.append(nueva_usuario)
nueva_usuario = Jugador('Alex', 'alex@turning.com', 'Zerg', 0)
jugadores.append(nueva_usuario)

def export_jugadores(jugadores):
    dict_jugadores = __jugadores_to_dict(jugadores)
    with open(__jugadores_archivo, 'w', 1) as archivo:
        json.dump(dict_jugadores, archivo)


def get_jugadores():
    jugadores = []
    with open(__jugadores_archivo, 'r', 1) as archivo_lectura:
        data = json.load(archivo_lectura)

    for usuario in data['jugadores']:
        jugadores.append(Jugador(usuario['nombre'], usuario['email'], usuario['raza'], usuario['puntos']))

    return jugadores


def __jugadores_to_dict(jugadores):
    dict_jugadores = {}
    lista_usuario = []
    for usuario in jugadores:
        lista_usuario.append({'nombre': usuario.get_nombre(), 'email': usuario.get_email(),
                              'raza': usuario.get_raza(), 'puntos': usuario.get_puntos()})
    dict_jugadores['jugadores'] = lista_usuario

    return dict_jugadores


export_jugadores(jugadores)
