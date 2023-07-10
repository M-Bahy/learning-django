from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request handeller
# request -> response
# view = action


def say_hello(request):
    return render(request, "hello.html")
