import unittest
import django
import sys
from django.test import Client
from django.urls import reverse

django.setup()

sys.path.append("playground")


class TestViews(unittest.TestCase):
    def test_home_view(self):
        client = Client()
        response = client.get(reverse("say_hello"))
        self.assertEqual(response.status_code, 200)
