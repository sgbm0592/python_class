import pytest

from proyecto_final.jugador.jugador import Jugador
from proyecto_final.partida.partida import Partida

@pytest.fixture
def jugador_1():
    nombre = 'Gaby'
    email = 'sgbm0592@gmail.com'
    raza = 'Terran'
    puntos = 1

    nueva_jugador = Jugador(nombre=nombre, email=email, raza=raza, puntos=puntos)

    return nueva_jugador


@pytest.fixture
def jugador_2():
    nombre = 'Gaby'
    email = 'sgbm0592@gmail.com'
    raza = 'Terran'
    puntos = 1

    nueva_jugador = Jugador(nombre=nombre, email=email, raza=raza, puntos=puntos)

    return nueva_jugador

def test_crear_partida(jugador_1, jugador_2):
    numero = 1

    nueva_partida = Partida(numero=numero,jugador_1=jugador_1, jugador_2=jugador_2)

    assert type(nueva_partida) == Partida
    assert nueva_partida.get_jugador_1() == jugador_1
    assert nueva_partida.get_jugador_2() == jugador_2


def test_elegir_ganador(jugador_1, jugador_2):
    numero = 1

    nueva_partida = Partida(numero=numero, jugador_1=jugador_1, jugador_2=jugador_2)
    nueva_partida.set_ganador(jugador_1)
    assert nueva_partida.get_ganador() == jugador_1



