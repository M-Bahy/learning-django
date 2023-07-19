from django.db import models


# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    duration = models.IntegerField()
    fees = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()


class StudentCourse(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    registration_date = models.DateField()
    status = models.CharField(max_length=50)
