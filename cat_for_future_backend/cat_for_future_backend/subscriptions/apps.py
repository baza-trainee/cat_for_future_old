from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class SubscriptionsConfig(AppConfig):
    name = "cat_for_future_backend.subscriptions"
    verbose_name = _("Subscriptions")
