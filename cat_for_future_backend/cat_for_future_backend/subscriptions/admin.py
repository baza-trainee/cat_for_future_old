from django.contrib import admin
from .models import Subscription


@admin.register(Subscription)  # Add the Subscroption model to the administrative interface
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "cat", "date_created")
    search_fields = ("cat",)
    date_hierarchy = "date_created"
