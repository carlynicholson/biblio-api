from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from rest_framework_jwt.settings import api_settings

# Our JWT Payload
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None,
                    first_name=None, last_name=None):
        if username is None:
            raise TypeError("Users must have a username")
        if email is None:
            raise TypeError("Users must have an email address")
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
            is_staff=False
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError("Superusers must have a password")
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  # <- 'auto_now_add' is for one-time use
    updated_at = models.DateTimeField(auto_now=True)  # <- 'auto_now' will repeatedly update

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    # Tells django that the UserManager class defined above
    # should manage all the objects of this type
    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def token(self):
        """
        Get user's token and pass to the API
        """
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        payload = jwt_payload_handler(self)
        token = jwt_encode_handler(payload)

        return token

