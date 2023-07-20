from django.views.generic import ListView
from models import Student


class Person(ListView):
    model = Student
