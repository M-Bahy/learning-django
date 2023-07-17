from django.urls import path
from . import views
from django.urls import include, path
from rest_framework import routers
from .views import WorkoutRoutineViewSet

router = routers.DefaultRouter()
router.register("workout-routines", WorkoutRoutineViewSet)
urlpatterns = [
    path("", views.hello_world),
    path("dashboard/", views.admin_dashboard),
    path(
        "workout-routines/",
        WorkoutRoutineViewSet.as_view({"post": "create", "get": "list"}),
        name="workout-routines",
    ),
    # path("hello/", views.say_hello),
]
