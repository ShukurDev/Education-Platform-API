from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class User(AbstractUser):
    # is_student = models.BooleanField(default=False)
    # is_teacher = models.BooleanField(default=False)
    class Meta:
        verbose_name = "users"

    ROLE = (
        (1, 'Admin'),
        (2, 'Manager'),
    )
    first_name = models.CharField(max_length=32, verbose_name="first name")
    last_name = models.CharField(max_length=32, verbose_name="last name")
    email = models.CharField(max_length=32, verbose_name="email")
    phone = models.CharField(max_length=32, verbose_name="phone")
    self_detail = models.TextField(verbose_name="self detail")
    is_superuser = models.BooleanField(default=False, verbose_name='Super user')
    is_staff = models.BooleanField(default=False, verbose_name='Staff user')
    is_active = models.BooleanField(default=True, verbose_name='Active user')
    is_verified = models.BooleanField(default=False, verbose_name='Verified user')
    role = models.IntegerField(choices=ROLE, default=2)
    date_login = models.DateTimeField(auto_now=True, verbose_name='Last login')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    # EMAIL_FIELD = 'email'
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
