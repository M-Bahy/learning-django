from django.shortcuts import render
from base.models import Person, Student, Course, StudentCourse
from serializers import (
    PersonSerializer,
    StudentSerializer,
    CourseSerializer,
    StudentCourseSerializer,
)
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
    check = Person.objects.filter(id=person_id)
    if check:
        return render(
            request,
            "delete.html",
            {"message": "Person with same ID already exists"},
        )
    item = Person.objects.create(id=person_id, name=name, age=age)
    item.save()
    return render(
        request,
        "delete.html",
        {"message": "Person added successfully"},
    )


@api_view(["POST"])
def add_db_s(request):
    id = request.POST.get("id")
    name = request.POST.get("name")
    age = request.POST.get("age")
    address = request.POST.get("address")
    phone = request.POST.get("phone")
    check = Student.objects.filter(id=id)
    if check:
        return render(
            request,
            "delete.html",
            {"message": "Student with same ID already exists"},
        )
    item = Student.objects.create(
        id=id, name=name, age=age, address=address, phone=phone
    )
    item.save()
    return render(
        request,
        "delete.html",
        {"message": "Student added successfully"},
    )


@api_view(["POST"])
def add_db_c(request):
    id = request.POST.get("id")
    name = request.POST.get("name")
    duration = request.POST.get("duration")
    fees = request.POST.get("fees")
    check = Course.objects.filter(id=id)
    if check:
        return render(
            request,
            "delete.html",
            {"message": "Course with same ID already exists"},
        )
    item = Course.objects.create(
        id=id, name=name, duration=duration, fees=fees
    )
    item.save()
    return render(
        request,
        "delete.html",
        {"message": "Course added successfully"},
    )


def say_hello(request):
    data = ["bharat", "rahul", "sachin"]
    return render(request, "hello.html", {"data": data})


def add_person(request):
    return render(request, "add.html")


def add_student(request):
    return render(request, "add_student.html")


def add_course(request):
    return render(request, "add_course.html")


def add_student_course(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    new = False
    for student in students:
        for course in courses:
            check = StudentCourse.objects.filter(
                student_id=student, course_id=course
            )
            if check:
                continue
            StudentCourse.objects.create(
                student_id=student, course_id=course, status="active"
            )
            new = True
    if new:
        return render(
            request,
            "delete.html",
            {"message": "StudentCourse added successfully"},
        )
    return render(
        request, "delete.html", {"message": "No new StudentCourse were added"}
    )


@api_view(["GET"])
def get_data(request):
    items = Person.objects.all()
    serializer = PersonSerializer(items, many=True)
    person = serializer.data
    items = Student.objects.all()
    serializer = StudentSerializer(items, many=True)
    student = serializer.data
    items = Course.objects.all()
    serializer = CourseSerializer(items, many=True)
    course = serializer.data
    items = StudentCourse.objects.all()
    serializer = StudentCourseSerializer(items, many=True)
    student_course = serializer.data
    return render(
        request,
        "hello.html",
        {
            "person": person,
            "student": student,
            "courses": course,
            "student_course": student_course,
        },
    )


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
    is_deleted = False
    if len(items) != 0:
        items.delete()
        is_deleted = True
    items = Student.objects.all()
    if len(items) != 0:
        items.delete()
        is_deleted = True
    items = Course.objects.all()
    if len(items) != 0:
        items.delete()
        is_deleted = True
    items = StudentCourse.objects.all()
    if len(items) != 0:
        items.delete()
        is_deleted = True
    if is_deleted:
        return render(
            request, "delete.html", {"message": "Deleted successfully"}
        )
    return render(request, "delete.html", {"message": "No data found"})
