from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField
from django.utils.translation import gettext_lazy as _

from cat_for_future_backend.users.managers import UserManager


class User(AbstractUser):
    """
    Default custom user model for cat_for_future_backend.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    name = CharField(_("Ім'я користувача"), blank=True, max_length=15)
    city = CharField(_("Місто"), blank=True, max_length=50)
    email = EmailField(_("Електронна адреса"), unique=True)
    phone_number = CharField(_("Номер телефону"), unique=True, null=True, blank=True, max_length=10)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    username = None  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
