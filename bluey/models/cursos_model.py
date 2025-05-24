from .repositories.cursos_repository import *

def get_courses():

    cursos = obtener_cursos_usuarios()

    # filtro la data


    return [dict(row) for row in cursos]