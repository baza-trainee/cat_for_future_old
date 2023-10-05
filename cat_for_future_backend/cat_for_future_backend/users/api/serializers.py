from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import serializers

from cat_for_future_backend.users.models import User as UserType
from cat_for_future_backend.subscriptions.models import Subscription


User = get_user_model()


class UserSerializer(serializers.ModelSerializer[UserType]):
    has_max_subscriptions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["name", "city", "phone_number", "email", "url", "has_max_subscriptions"]

    def get_has_max_subscriptions(self, obj):
        # Define your maximum subscription count threshold here
        subscription_count = Subscription.objects.filter(user=obj).count()
        return subscription_count >= settings.MAX_SUBSCRIPTION_PER_USER
