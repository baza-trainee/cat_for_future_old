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

router.register("users", UserViewSet)
router.register("cats", CatViewSet)
router.register("histories", HistoryViewSet)
router.register("subscriptions", SubscriptionViewSet)

app_name = "api"
urlpatterns = router.urls
