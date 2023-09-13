from rest_framework import serializers

from cat_for_future_backend.subscriptions.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["user", "cat", "created_at"]
        readonly_fields = ["created_at"]
