from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class HabitApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_unauthorized_user_cannot_access_habits(self):
        """
        Проверяет, что неавторизованный пользователь получает ошибку 401.
        """
        response = self.client.get('/api/habits/')
        self.assertEqual(response.status_code, 401)

    def test_authorized_user_can_access_habits(self):
        """
        Проверяет, что авторизованный пользователь может получить доступ к своим привычкам.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/habits/')
        self.assertEqual(response.status_code, 200)
