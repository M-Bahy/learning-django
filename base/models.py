from django.db import models


# Create your models here.
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    fees = models.IntegerField()


class StudentCourse(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
