from django.shortcuts import render
from base.models import Person
from serializers import PersonSerializer
from rest_framework.decorators import api_view
from random import Random
from faker import Faker
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
    View,
    FormView,
)
import django

django.setup()

fake = Faker()


class AllPeople(ListView):
    model = Person
    template_name = "person_list.html"
    # template_name = "add.html"


@api_view(["POST"])
def add_db(request):
    person_id = request.POST.get("id")
    name = request.POST.get("name")
    age = request.POST.get("age")
    item = Person.objects.create(id=person_id, name=name, age=age)
    item.save()
    return render(
        request,
        "delete.html",
        {"message": "Person added successfully"},
    )


def say_hello(request):
    data = ["bharat", "rahul", "sachin"]
    return render(request, "hello.html", {"data": data})


def add_person(request):
    # id = Random().randint(1, 100)
    # name = fake.name()
    # age = Random().randint(1, 100)
    # Person.objects.create(id=id, name=name, age=age)
    # return render(
    #     request, "delete.html", {"message": "Person added successfully"}
    # )
    return render(request, "add.html")


@api_view(["GET"])
def get_data(request):
    items = Person.objects.all()
    serializer = PersonSerializer(items, many=True)
    data = serializer.data
    return render(request, "hello.html", {"data": data})


@api_view(["GET"])
def get_one(request, id):
    try:
        item = Person.objects.get(id=id)
        serializer = PersonSerializer(item)
        data = serializer.data
        return render(request, "one.html", {"data": data})
    except Exception:
        return render(request, "one.html")


def delete_one(request, id):
    try:
        item = Person.objects.get(id=id)
        item.delete()
        return render(
            request, "delete.html", {"message": "Person deleted successfully"}
        )
    except Exception:
        return render(request, "delete.html", {"message": "Person not found"})


def delete_all(request):
    items = Person.objects.all()
    if len(items) != 0:
        items.delete()
        return render(
            request, "delete.html", {"message": "Deleted successfully"}
        )
    return render(request, "delete.html", {"message": "No data found"})
