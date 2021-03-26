import json

from poo.tarea.tarea import Tarea
from poo.usuario.usuario import Usuario

__tareas_archivo='tareas.json'


datos = {
    'tareas': []
}
tareas = datos['tareas']
nueva_tarea = Tarea('Agrgar Usuario', 'Agregar como usuarios a los alumnos de QA Minds', 'Alta', Usuario('Gaby', 'sgbm0592@gmail.com'))
tareas.append(nueva_tarea)
nueva_tarea = Tarea('Eliminar Usuario', 'Permitir eliminar usuarios del sistema', 'Media', Usuario('Adolfo', 'adolfo@gmail.com'))
tareas.append(nueva_tarea)
nueva_tarea = Tarea('Listar Usuario', 'Listar todos los alumnos de QA Minds', 'Baja', Usuario('Juan', 'juan@mail.com'))
tareas.append(nueva_tarea)

def export_tareas(tareas):
    dict_tareas = __tareas_to_dict(tareas)
    with open(__tareas_archivo, 'w') as archivo:
        json.dump(dict_tareas, archivo)

def get_tareas():
    tareas = []
    with open(__tareas_archivo, 'r') as archivo_lectura:
        data = json.load(archivo_lectura)

    for tarea in data['tareas']:
        tareas.append(Tarea(tarea['titulo'], tarea['descripcion'],
                            tarea['prioridad'],
                            Usuario(tarea['usuario']['nombre'], tarea['usuario']['email'])))

    return tareas

def __tareas_to_dict(tareas):
    dict_tareas = {}
    lista_tarea = []
    for tarea in tareas:
        usuario =tarea.get_usuario()
        lista_tarea.append({'titulo': tarea.get_titulo(), 'descripcion': tarea.get_descripcion(),
                            'prioridad': tarea.get_prioridad(),
                            'estado': tarea.get_estado(),
                            'usuario':{'nombre': usuario.get_nombre(), 'email': usuario.get_email()}})
    dict_tareas['tareas'] = lista_tarea

    return dict_tareas