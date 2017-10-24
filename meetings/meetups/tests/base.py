from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase, APIClient

from authentication.models import Token


class BaseApiTestCase(APITestCase):
    @staticmethod
    def create_user(username, password):
        user = get_user_model().objects.create(username=username)
        user.set_password(password)
        user.save()
        return user

    def setUp(self):
        self.client = APIClient()
        self.client.login()

        self.authenticated_user = self.create_user('test_username1', 'test_password1')
        self.not_authenticated_user = self.create_user('test_username2', 'test_password2')

        token = Token.objects.get(user__username='test_username1')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
