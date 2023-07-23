# map urls to view functions
from django.urls import path
import sys

sys.path.append("playground")
import views

urlpatterns = [
    path("", views.get_data, name="get_data"),
    path("hi", views.say_hello, name="say_hello"),
    path("<int:id>/", views.get_one, name="get_one"),
    path("delete/<int:id>/", views.delete_one, name="delete_one"),
    path("add/person", views.add_person, name="add_person"),
    path("delete", views.delete_all, name="delete_all"),
    path("person", views.AllPeople.as_view()),
    path("add/add_db", views.add_db, name="add_db"),
    path("add/student", views.add_student, name="add_student"),
    path("add/add_db_s", views.add_db_s, name="add_db_s"),
    path("add/course", views.add_course, name="add_course"),
    path("add/add_db_c", views.add_db_c, name="add_db_c"),
    path("add/sc", views.add_student_course, name="add_student_course"),
]
