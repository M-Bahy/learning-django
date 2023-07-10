# map urls to view functions
from django.urls import path
from . import views

urlpatterns = [path("", views.say_hello)]
