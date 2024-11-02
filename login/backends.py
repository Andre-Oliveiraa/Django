from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class authPorEmail(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            try:
                user = UserModel.objects.get(email=username)
            except UserModel.DoesNotExist:
                return None
        if user.check_password(password) and self.user_can_authenticate(user):
            return user