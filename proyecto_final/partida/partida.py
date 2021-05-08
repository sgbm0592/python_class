class Partida:


    def __init__(self, numero, jugador_1, jugador_2):
        self.__numero = numero
        self.__jugador_1 = jugador_1
        self.__jugador_2 = jugador_2

    def __repr__(self):
        return '[ {} - {} - {} ]'.format(self.__numero, self.__jugador_1, self.__jugador_2)

    def get_numero(self):
        return self.__numero

    def get_jugador_1(self):
        return self.__jugador_1

    def get_jugador_2(self):
        return self.__jugador_2

    def get_ganador(self):
        return self.__ganador

    def set_jugador_1(self, jugador_1):
        self.__jugador_1 = jugador_1

    def set_jugador_2(self, jugador_2):
        self.__jugador_2 = jugador_2

    def set_ganador(self, ganador):
        self.__ganador = ganador