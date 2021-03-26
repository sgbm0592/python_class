class Usuario:

    def __init__(self, nombre, email):
        self.__nombre = nombre
        self.__email = email

    def __repr__(self):
        return '{} - {}'.format(self.__nombre, self.__email)

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_email(self, email):
        self.__email = email

