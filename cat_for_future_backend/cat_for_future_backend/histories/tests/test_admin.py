from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import History


class TestHistoryAdmin(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password="password",
        )
        cls.history = History.objects.create(
            title="Test History",
            content="This is a test history entry.",
        )

    def setUp(self):
        self.client.login(email="admin@example.com", password="password")

    def test_changelist(self):
        url = reverse("admin:histories_history_changelist")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        url = reverse("admin:histories_history_changelist")
        response = self.client.get(url, data={"q": "Test History"})
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        url = reverse("admin:histories_history_add")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            url,
            data={
                "title": "New History Entry",
                "content": "This is a new history entry.",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(History.objects.filter(title="New History Entry").exists())

    def test_view_history(self):
        url = reverse("admin:histories_history_change",
                      args=[self.history.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
