from poo.tarea.tarea import Tarea
from poo.usuario.usuario import Usuario


def test_crear_tarea():
    titulo = 'Test Titulo'
    descripcion = 'Test Descripcion'
    prioridad = 1
    usuario = Usuario('Test', 'test@mail.com')
    estado = Tarea.BACKLOG
    tarea = Tarea(titulo, descripcion, prioridad, usuario)

    assert titulo == tarea.get_titulo()
    assert descripcion == tarea.get_descripcion()
    assert prioridad == tarea.get_prioridad()
    assert usuario == tarea.get_usuario()
    assert estado == tarea.get_estado()
    assert type(usuario) == Usuario
    assert isinstance(tarea.get_usuario(), Usuario)