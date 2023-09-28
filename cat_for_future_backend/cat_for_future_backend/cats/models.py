from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Cat(models.Model):
    name = models.CharField(_("Кличка"), blank=True, max_length=15)
    age = models.IntegerField(_("Вік"), null=True, blank=True)
    sex = models.CharField(_("Стать"), max_length=10, choices=[("male", "Хлопчик"), ("female", "Дівчинка")])
    date_created = models.DateTimeField(_("Дата створення"), auto_now_add=True)
    update_date = models.DateTimeField(_("Дата оновлення"), auto_now=True)
    booking_status = models.BooleanField(_("Стан заброньованості"), default=False)
    photo = models.ImageField(_("Фото"), upload_to="photos/", blank=True, null=True)

    def __str__(self):
        return self.name
