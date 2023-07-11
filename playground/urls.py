# map urls to view functions
from django.urls import path

import sys

sys.path.append("playground")
import views

urlpatterns = [path("", views.say_hello, name="say_hello")]
