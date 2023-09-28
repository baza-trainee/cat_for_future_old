from factory import SubFactory, Faker, LazyFunction
import random
from factory.django import DjangoModelFactory
from django.contrib.auth import get_user_model
from cat_for_future_backend.subscriptions.models import Subscription
from cat_for_future_backend.cats.models import Cat


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = Faker("email")
    password = "testpassword"  # Set a default password for testing purposes


class CatFactory(DjangoModelFactory):
    class Meta:
        model = Cat

    @classmethod
    def random_name(cls):
        names = [
            "Whiskers",
            "Fluffy",
            "Mittens",
            "Spike",
            "Felix",
        ]
        return random.choice(names)

    name = LazyFunction(lambda: CatFactory.random_name())
    age = Faker("random_int", min=1, max=20)
    sex = Faker("random_element", elements=("Male", "Female"))

    @classmethod
    def create(cls, **kwargs):
        kwargs["name"] = cls.random_name()
        return super().create(**kwargs)


class SubscriptionFactory(DjangoModelFactory):
    class Meta:
        model = Subscription

    user = SubFactory(UserFactory)
    cat = SubFactory(CatFactory)
