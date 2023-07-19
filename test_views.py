import unittest
import django
from django.test import Client
from django.urls import reverse

django.setup()


class TestViews(unittest.TestCase):
    def test_home_view(self):
        client = Client()
        response = client.get(reverse("say_hello"))
        self.assertEqual(response.status_code, 200)
