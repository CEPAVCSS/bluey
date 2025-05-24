from ..sqlite import get_connection


def obtener_cursos_usuarios():
    """
        Repositorio
    """

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cursos")
    cursos = cursor.fetchall()
    conn.close()

    return cursos
