from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework import viewsets
from .models import WorkoutRoutine
from .serializers import WorkoutRoutineSerializer


class WorkoutRoutineViewSet(viewsets.ModelViewSet):
    queryset = WorkoutRoutine.objects.all()
    serializer_class = WorkoutRoutineSerializer


@api_view(["GET"])
def hello_world(request):
    # return Response({"message": "Hello, world!"})
    return render(request, "admin_home.html")


@api_view(["GET"])
def admin_dashboard(request):
    return render(request, "admin_dashboard.html")
