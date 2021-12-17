from django.db import models
from profileapp.models import Student
from courseapp.models import CourseModel
from django.utils.translation import gettext as _


# Create your models here.

class OrderModel(models.Model):
    student = models.ForeignKey(Student, related_name="order", on_delete=models.CASCADE)
    courses = models.ForeignKey(CourseModel, related_name="order", on_delete=models.CASCADE)

    ordered_at = models.DateTimeField(auto_now_add=True, verbose_name=_("ordered at"))
