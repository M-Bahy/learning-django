import unittest
import django
import sys

django.setup()

sys.path.append("playground")

from django.urls import resolve, reverse

from views import (
    say_hello,
    get_data,
    get_one,
    delete_one,
    add_person,
    delete_all,
    add_db,
    add_student,
    add_db_s,
    add_course,
    add_db_c,
)


class TestUrls(unittest.TestCase):
    def test_empty_path_is_resolved(self):
        url = reverse("say_hello")
        self.assertEqual(resolve(url).func, say_hello)

    def test_get_data_is_resolved(self):
        url = reverse("get_data")
        self.assertEqual(resolve(url).func, get_data)

    def test_get_one_is_resolved(self):
        url = reverse("get_one", args=[1])
        self.assertEqual(resolve(url).func, get_one)

    def test_delete_one_is_resolved(self):
        url = reverse("delete_one", args=[1])
        self.assertEqual(resolve(url).func, delete_one)

    def test_add_person_is_resolved(self):
        url = reverse("add_person")
        self.assertEqual(resolve(url).func, add_person)

    def test_delete_all_is_resolved(self):
        url = reverse("delete_all")
        self.assertEqual(resolve(url).func, delete_all)

    def test_add_db_is_resolved(self):
        url = reverse("add_db")
        self.assertEqual(resolve(url).func, add_db)

    def test_add_student_is_resolved(self):
        url = reverse("add_student")
        self.assertEqual(resolve(url).func, add_student)

    def test_add_db_s_is_resolved(self):
        url = reverse("add_db_s")
        self.assertEqual(resolve(url).func, add_db_s)

    def test_add_course_is_resolved(self):
        url = reverse("add_course")
        self.assertEqual(resolve(url).func, add_course)

    def test_add_db_c_is_resolved(self):
        url = reverse("add_db_c")
        self.assertEqual(resolve(url).func, add_db_c)
