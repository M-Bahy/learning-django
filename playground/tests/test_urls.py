import unittest
import sys
from django.test import SimpleTestCase
import os

# from django.conf import settings

# sys.path.append("myapp")
import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
# settings.configure()

sys.path.append("playground")
from django.urls import resolve, reverse
from views import say_hello


class TestUrls(unittest.TestCase):
    def test_empty_path_is_resolved(self):
        url = reverse("say_hello")
        self.assertEqual(resolve(url).func, say_hello)


unittest.main()
