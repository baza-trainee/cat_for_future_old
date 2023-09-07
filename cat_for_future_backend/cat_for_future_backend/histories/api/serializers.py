from rest_framework import serializers

from cat_for_future_backend.histories.models import History


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'
