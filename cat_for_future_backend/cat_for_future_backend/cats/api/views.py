from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from .serializers import CatSerializer
from cat_for_future_backend.cats.models import Cat


class CatViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = CatSerializer
    queryset = Cat.objects.all()
    lookup_field = "pk"
