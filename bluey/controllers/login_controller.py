from bluey.models import user_model

def validate_login(username, password):
    return user_model.check_user_credentials(username, password)