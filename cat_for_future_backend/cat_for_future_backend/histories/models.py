from django.db import models
from django.db.models import CharField, TextField, DateTimeField
from django.utils.translation import gettext_lazy as _


class History(models.Model):
    """
    Model for representing the happy history of users who have taken the cat
    """

    title = CharField(_("Заголовок"), max_length=50, blank=False)
    content = TextField(_("Текст історії"), blank=False)
    date_created = DateTimeField(_("Дата створення"), auto_now_add=True, blank=False)

    def __str__(self):
        """
        Returns a string representation of history object
        """

        return self.title
