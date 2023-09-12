from rest_framework import serializers
from cat_for_future_backend.cats.models import Cat


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cat
        fields = ["id", "name", "age", "sex", "date_created", "update_date", "booking_status", "photo"]
        read_only_fields = ["date_created", "update_date"]
