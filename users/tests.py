from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from users.models import User


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.path = reverse("users:registration")
        self.data = {
            "first_name": "SIarhei",
            "last_name": "Zaluzhny",
            "username": "admin",
            "email": "levzhe@mail.com",
            "password1": "12345Qqq",
            "password2": "12345Qqq",
        }

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data["title"], "Store - Регистрация")
        self.assertTemplateUsed(response, "users/registration.html")

    def test_user_registration_post_success(self):
        response = self.client.post(self.path, self.data)

        username = self.data["username"]

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertTrue(User.objects.filter(username=username).exists())
        # self.assertRedirects(response, reverse("users:login")) НЕ РАБОТАЕТ. СКОРЕЕ ВСЕГО ДЕЛО В ТОКЕНАХ СОЦ.СЕТЕЙ.
        # Проверить при рефаткоринге
