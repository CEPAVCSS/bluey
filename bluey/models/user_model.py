
from .repositories.user_repository import *



def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper



@decorator
def check_user_credentials(username, password):
    # consultar una base de datos
    user = get_user_by_username(username)

    if user == None:
        return False, None, None

    role = user["role_name"]
    # role = user["role_name"]
    # role = "admin"  # Cambiar esto por la consulta a la base de datos

    if user:
        # db_username, db_password = user
        return True, role, user
    
    else:
        # Si no se encuentra el usuario, se puede retornar False o lanzar una excepción
        return False
    
    # return username == "admin" and password == "1234"


