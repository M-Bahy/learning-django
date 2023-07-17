from django.shortcuts import render


# Create your views here.
# request handeller
# request -> response
# view = action


def say_hello(request):
    return render(request, "hello.html", {"name": "Rahul"})
