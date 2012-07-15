import uuid
from django.contrib.auth.models import User

def generate_username(user, profile, client):
    user_info = client.get_user_info()
    username = user_info.get('screen_name', None)
    try:
        user = User.objects.get(username = username)
        if user:
            username = str(uuid.uuid4())[:30]
    except User.DoesNotExist:
        pass
    return username
