from proyecto_final.jugador.jugador import Jugador


def test_crear_jugador():
    nombre = 'Gaby'
    email = 'sgbm0592@gmail.com'
    raza = 'Terran'
    puntos = 1

    nueva_jugador = Jugador(nombre=nombre, email=email, raza=raza, puntos=puntos)

    assert type(nueva_jugador) == Jugador
    assert nueva_jugador.get_email() == email
    assert nueva_jugador.get_raza() == raza
    assert nueva_jugador.get_puntos() == puntos


def test_agregar_puntos():
    nombre = 'Gaby'
    email = 'sgbm0592@gmail.com'
    raza = 'Terran'
    puntos = 4

    nuevo_jugador = Jugador(nombre=nombre, email=email, raza=raza, puntos=puntos)

    assert type(nuevo_jugador) == Jugador
    nuevos_puntos = puntos + 3
    nuevo_jugador.set_puntos(nuevos_puntos)
    assert nuevo_jugador.get_puntos() == nuevos_puntos



