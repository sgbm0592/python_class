import json
from poo.usuario.usuario import Usuario

__usuarios_archivo='usuarios.json'


datos = {
    'usuarios': []
}
usuarios = datos['usuarios']
nueva_usuario =  Usuario('Gaby', 'sgbm0592@gmail.com')
usuarios.append(nueva_usuario)
nueva_usuario = Usuario('Adolfo', 'adolfo@gmail.com')
usuarios.append(nueva_usuario)
nueva_usuario = Usuario('Juan', 'juan@mail.com')
usuarios.append(nueva_usuario)


def export_usuarios(usuarios):
    dict_usuarios = __usuarios_to_dict(usuarios)
    with open(__usuarios_archivo, 'w') as archivo:
        json.dump(dict_usuarios, archivo)


def get_usuarios():
    usuarios = []
    with open(__usuarios_archivo, 'r') as archivo_lectura:
        data = json.load(archivo_lectura)

    for usuario in data['usuarios']:
        usuarios.append(Usuario(usuario['nombre'], usuario['email']))

    return usuarios


def __usuarios_to_dict(usuarios):
    dict_usuarios = {}
    lista_usuario = []
    for usuario in usuarios:
        lista_usuario.append({'nombre': usuario.get_nombre(), 'email': usuario.get_email()})
    dict_usuarios['usuarios'] = lista_usuario

    return dict_usuarios

get_usuarios()