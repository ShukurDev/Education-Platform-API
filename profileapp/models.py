from django.db import models
from courseapp.models import CourseModel
from accounts.models import User
from django.utils.translation import gettext as _


# Create your models here.

class Student(models.Model):
    student_user = models.ForeignKey(User, related_name="student", on_delete=models.CASCADE)
    student_course = models.OneToOneField(CourseModel, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32, verbose_name=_("first name"), null=True, blank=True)
    last_name = models.CharField(max_length=32, verbose_name=_("last name"), null=True, blank=True)
    email = models.CharField(max_length=32, verbose_name=_("email"), null=True, blank=True)
    phone = models.CharField(max_length=13, verbose_name=_("phone"))
    self_detail = models.TextField(verbose_name=_("self detail"))
    avatar = models.ImageField(upload_to="images", null=True, blank=True)
    purpose = models.CharField(max_length=128, verbose_name=_("purpose"))
    interests = models.CharField(max_length=128, verbose_name=_("interests"))

    def __str__(self):
        return self.first_name


class Teacher(models.Model):
    teacher_user = models.ForeignKey(User, related_name="techers", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32, verbose_name=("first name"))
    last_name = models.CharField(max_length=32, verbose_name=("last name"))
    email = models.CharField(max_length=32, verbose_name=("email"))
    phone = models.CharField(max_length=13, verbose_name=("phone"))
    self_detail = models.TextField(verbose_name=("self detail"))
    avatar = models.ImageField(upload_to="images")
    purpose = models.CharField(max_length=128, verbose_name=("purpose"))
    portfolio = models.FileField(upload_to="files/portfolio")

    def __str__(self):
        return self.first_name
