import unittest
import django
import sys

django.setup()

sys.path.append("playground")

from django.urls import resolve, reverse

from views import say_hello


class TestUrls(unittest.TestCase):
    def test_empty_path_is_resolved(self):
        url = reverse("say_hello")
        self.assertEqual(resolve(url).func, say_hello)
