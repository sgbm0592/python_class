class Jugador:


    TERRAN = 'Terran'
    ZERG = 'Zerg'
    PROTOSS = 'Protoss'

    def __init__(self, nombre, email, raza, puntos):
        self.__nombre = nombre
        self.__email = email
        self.__raza = raza
        self.__puntos = puntos

    def __repr__(self):
        return '{} - {} - {} - {} '.format(self.__nombre, self.__email, self.__raza, self.__puntos)

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

    def get_raza(self):
        return self.__raza

    def get_puntos(self):
        return self.__puntos

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_email(self, email):
        self.__email = email

    def set_raza(self, raza):
        self.__raza = raza

    def set_puntos(self, puntos):
        self.__puntos = puntos