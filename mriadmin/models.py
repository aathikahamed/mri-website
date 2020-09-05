from django.db import models
from django.contrib.auth.models import AbstractUser


class News(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(upload_to='news_images')

    def __str__(self):
        return self.title


class Calendar(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title


class User(AbstractUser):
    birth_date = models.DateField(null=True)
    teachers_nic = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    joined_date = models.DateField(auto_now_add=True)


class Class_room(models.Model):
    class_teacher = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    class_name = models.CharField(max_length=128)

    def __str__(self):
        return self.class_name


class Student(models.Model):
    name = models.CharField(max_length=128)
    date_of_birth = models.DateField()
    email_address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    joined_date = models.DateField(auto_now_add=True)
    fathers_name = models.CharField(max_length=128)
    fathers_nic = models.CharField(max_length=64)
    mothers_name = models.CharField(max_length=128)
    mothers_nic = models.CharField(max_length=64)

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    active = models.BooleanField(default=True)
    class_room = models.ForeignKey(
        Class_room, on_delete=models.SET_NULL, null=True, related_name='class_room')

    def __str__(self):
        return self.name


class Exam(models.Model):
    exam_name = models.CharField(max_length=128)
    exam_date = models.DateTimeField(auto_now_add=True)
    teacher_in_charge = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.exam_name} on {self.exam_date}'


class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    marks = models.IntegerField()
    exam = models.ForeignKey(Exam, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.student} got {self.marks} for {self.exam}'
