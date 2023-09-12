from django.contrib import admin
from django.utils.translation import gettext as _

from .models import History


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ["title", "date_created"]
    search_fields = ["title"]
    ordering = ["-date_created"]
    fieldsets = (
        (None, {"fields": ("title", "content")}),
    )
