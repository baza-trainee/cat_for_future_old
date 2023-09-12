from django.contrib import admin
from .models import Cat


@admin.register(Cat)  # Add the Cat model to the administrative interface
class CatAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "sex", "date_created", "update_date", "booking_status")
    list_filter = ("sex", "booking_status")
    search_fields = ("name",)
    list_editable = ("age", "booking_status")
    date_hierarchy = "date_created"


# admin.site.register(Cat, CatAdmin)  # Register the Cat model in the administrative interface
