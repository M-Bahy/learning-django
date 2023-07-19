from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonSerializer
from base.models import Person


@api_view(["GET"])
def get_data(request):
    items = Person.objects.all()
    serializer = PersonSerializer(items, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_person(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
