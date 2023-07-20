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
    path("add", views.add_person, name="add_person"),
    path("delete", views.delete_all, name="delete_all"),
    path("person", views.AllPeople.as_view()),
    path("add_db", views.add_db, name="add_db"),
]
