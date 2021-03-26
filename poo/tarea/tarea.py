import json

class Tarea:

    BACKLOG = 'Backlog'
    TODO = 'ToDo'
    DOING = 'Doing'
    RESOLVED = 'Resolved'

    def __init__(self, titulo, descripcion, prioridad, usuario):
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__prioridad = prioridad
        self.__usuario = usuario
        self.estado = self.BACKLOG

    def __repr__(self):
        return '\n\ttitulo:{}\n\tdescripcion:{}\n\tprioridad:{}\n\testado:{}\n\tUsuario:({})'.format(self.__titulo,
                                                                                           self.__descripcion,
                                                                                           self.__prioridad,
                                                                                           self.estado,
                                                                                           self.__usuario)

    def get_titulo(self):
        return self.__titulo

    def get_descripcion(self):
        return self.__descripcion

    def get_prioridad(self):
        return self.__prioridad

    def get_usuario(self):
        return self.__usuario

    def get_estado(self):
        return self.estado

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def set_prioridad(self, prioridad):
        self.__prioridad = prioridad

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def set_estado(self, estado):
        self.estado = estado