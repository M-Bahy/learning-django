# learn-django
install django
```bash
pip install django
```
create a django project in the current directory
```bash
django-admin startproject myapp .
```
run the server (taking into account the settings in the settings.py file)
```bash
python manage.py runserver
```
By default, the server runs on port 8000. To change the port, specify it in the command
```bash
python manage.py runserver 8080
```
create a new django app
```bash
python manage.py startapp playground
```
In urls.py in your primary app (myapp) map the "/"'s to the appropriate handler files (it is like middleware in express)
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("playground.urls")),
]
```
Now in playground/urls.py, map the "/"'s to the appropriate function in views.py
```python
from django.urls import path
from . import views

urlpatterns = [path("", views.say_hello)]
```
Now in playground/views.py, create the function that will handle the request and return the response.
```python
from django.shortcuts import render
from django.http import HttpResponse
# request -> response
def say_hello(request):
    return render(request, "hello.html")
```
put the html file in the templates folder (playground/templates/hello.html)

# Note:
write your configurations in the .env file