from rest_framework import status, viewsets
from rest_framework.response import Response
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework.permissions import AllowAny

from .serializers import CatSerializer
from cat_for_future_backend.cats.models import Cat


class CatViewSet(viewsets.ModelViewSet):
    serializer_class = CatSerializer
    queryset = Cat.objects.all()

    def list_all(self):
        cats = self.queryset
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomSwaggerView(SpectacularSwaggerView):
    permission_classes = [AllowAny]
