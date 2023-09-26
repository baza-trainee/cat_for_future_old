from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from .serializers import SubscriptionSerializer
from cat_for_future_backend.subscriptions.models import Subscription


class SubscriptionViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    lookup_field = "pk"
