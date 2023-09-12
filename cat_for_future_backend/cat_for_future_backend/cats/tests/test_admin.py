from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase

from cat_for_future_backend.cats.models import Cat


class TestCatAdmin(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password="password",
        )
        cls.cat = Cat.objects.create(
            name="Test Cat",
            age=3,
            sex="male",
            booking_status=True,
        )

    def setUp(self):
        self.client.login(email="admin@example.com", password="password")

    def test_changelist(self):
        url = reverse("admin:cats_cat_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        url = reverse("admin:cats_cat_changelist")
        response = self.client.get(url, data={"q": "Test Cat"})
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        url = reverse("admin:cats_cat_add")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            url,
            data={
                "name": "New Cat",
                "age": 2,
                "sex": "female",
                "booking_status": False,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Cat.objects.filter(name="New Cat").exists())

    def test_view_cat(self):
        url = reverse("admin:cats_cat_change", args=[self.cat.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
