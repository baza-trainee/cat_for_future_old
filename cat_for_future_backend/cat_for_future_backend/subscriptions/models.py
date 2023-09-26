from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import ForeignKey, DateTimeField
from django.contrib.auth import get_user_model

from .managers import SubscriptionManager
from cat_for_future_backend.cats.models import Cat

User = get_user_model()


class Subscription(models.Model):
    """
    Model for representing the user's subscription to cat
    """

    user = ForeignKey(User, verbose_name="Потенційний хазяїн", on_delete=models.CASCADE)
    cat = ForeignKey(Cat, verbose_name="Кіт", on_delete=models.CASCADE)
    date_created = DateTimeField(_("Дата підписки"), auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} subscribed to {self.cat.name} on {self.date_created}"

    objects = SubscriptionManager()

    def save(self, *args, **kwargs):
        self.full_clean()  # Perform validation before saving
        super().save(*args, **kwargs)
