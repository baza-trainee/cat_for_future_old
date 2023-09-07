from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin

from .serializers import HistorySerializer
from cat_for_future_backend.histories.models import History
from rest_framework.viewsets import GenericViewSet


class HistoryViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = HistorySerializer
    queryset = History.objects.all()
    lookup_field = "pk"
