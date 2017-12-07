# coding=utf-8

from django.urls import reverse
from django.test import TestCase

from django.contrib.auth import get_user_model

User = get_user_model()


class TestUser(TestCase):
    def setUp(self):
        # init user
        user1 = User.objects.create_user(username='jason', password='123456')
        user2 = User.objects.create_user(username='lj', password='123', avatar='x1.path')
        user3 = User.objects.create_user(username='tom', password='123', avatar='x2.path')
        user4 = User.objects.create_user(username='arc', password='123', avatar='x3.path')

    def test_list(self):
        url = reverse("user-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)



