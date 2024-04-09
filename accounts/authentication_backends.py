# authentication_backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

CustomUser = get_user_model()

class CustomUserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None
