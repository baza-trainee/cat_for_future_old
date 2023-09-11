from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CatsConfig(AppConfig):
    name = "cat_for_future_backend.cats"
    verbose_name = _("Cats")
