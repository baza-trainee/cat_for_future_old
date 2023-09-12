from django.urls import path, include
from rest_framework.routers import DefaultRouter
from cat_for_future_backend.cats.api.views import CatViewSet, CustomSwaggerView

# Create a DefaultRouter object to automatically create a URL for the viewset
router = DefaultRouter()
router.register(r'cats', CatViewSet)

urlpatterns = [
    # We add URL paths using router.urls
    path('', include(router.urls)),
    # Add the URL for Swagger if you want to use drf-spectacular
    path('swagger/', CustomSwaggerView.as_view(), name='swagger'),
]
