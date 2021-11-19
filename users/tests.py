from django.test import TestCase
from django.urls import resolve, reverse
from rest_framework import status

from users.models import Account


class AccountTestCase(TestCase):
    def setUp(self):
        Account.objects.create(email="john_doe@email.com", password="#mypassword")
        Account.objects.create(email="jane_doe@email.com", password="#mypassword")
        Account.objects.create(email="johnnie_doe@email.com", password="#mypassword")

    def test_create_account(self):
        data = {
            "email": "janet@email.com",
            "password": "akdgasldaddddhjd",
            "confirm_password": "akdgasldaddddhjd"
        }
        data_2 = {

        }
        data_3 = {
            "email": "janet@email.com",
            "password": "akdgasldadaddddhjdhjsd",
            "confirm_password": "akdgasldaddddhjd"
        }
        response = self.client.post(reverse("user-create-account"), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_2 = self.client.post(reverse("user-create-account"), data=data_2, format='json')
        self.assertEqual(response_2.status_code, status.HTTP_400_BAD_REQUEST)

        response_3 = self.client.post(reverse("user-create-account"), data=data_3, format='json')
        self.assertEqual(response_3.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login(self):
        ...

