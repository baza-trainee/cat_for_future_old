from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from cat_for_future_backend.users.api.views import UserViewSet
from cat_for_future_backend.cats.api.views import CatViewSet
from cat_for_future_backend.histories.api.views import HistoryViewSet
from cat_for_future_backend.subscriptions.api.views import SubscriptionViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet, basename="users")
router.register("cats", CatViewSet, basename="cats")
router.register("histories", HistoryViewSet, basename="histories")
router.register("subscriptions", SubscriptionViewSet, basename="subscriptions")

app_name = "api"
urlpatterns = router.urls
