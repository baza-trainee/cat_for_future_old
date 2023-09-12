import pytest
from cat_for_future_backend.subscriptions.models import Subscription
from cat_for_future_backend.subscriptions.tests.factories import SubscriptionFactory, CatFactory, UserFactory
from django.core.exceptions import ValidationError

MAX_SUBSCRIPTION_PER_USER = 2

@pytest.mark.django_db
class TestSubscriptionManager:
    @pytest.fixture
    def test_user(self):
        return UserFactory()

    @pytest.fixture
    def test_cats(self):
        # Create a list of CatFactory instances based on MAX_SUBSCRIPTION_PER_USER
        return [CatFactory() for _ in range(MAX_SUBSCRIPTION_PER_USER)]

    def test_create_subscription(self, test_user, test_cats):
        # Create test subscriptions using factories
        for cat in test_cats:
            SubscriptionFactory(user=test_user, cat=cat)

        # Check if the user has the correct number of subscriptions
        subscriptions = Subscription.objects.filter(user=test_user)
        assert subscriptions.count() == MAX_SUBSCRIPTION_PER_USER

    def test_create_subscription_limit_exceeded(self, test_user, test_cats):
        # Create a subscription manager instance
        subscription_manager = Subscription.objects

        # Create test subscriptions up to the limit
        for cat in test_cats[:MAX_SUBSCRIPTION_PER_USER]:
            subscription_manager.create_subscription(user=test_user, cat=cat)

        # Attempt to create a subscription exceeding the limit
        with pytest.raises(ValidationError):
            error_subscription = subscription_manager.create_subscription(user=test_user, cat=test_cats[0])

