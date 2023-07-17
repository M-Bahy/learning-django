from rest_framework import serializers
from .models import WorkoutRoutine


class WorkoutRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutRoutine
        fields = ("id", "name", "description", "created_at")
