from django.contrib import admin

# Register your models here.
from .models import Student,Teacher
# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
