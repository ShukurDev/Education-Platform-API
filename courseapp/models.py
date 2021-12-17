from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
from accounts.models import User


class CourseModel(models.Model):
    objects = None
    title = models.CharField(max_length=56, verbose_name=_("title"))
    description = models.CharField(max_length=128, verbose_name=_("description"))
    price = models.FloatField(default=0.0, verbose_name=_("price"))
    video = models.FileField("files/video", null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))

    def __str__(self):
        return self.title


class CommentModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey("CourseModel", on_delete=models.CASCADE)
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))

    def __str__(self):
        return self.comment[:10]

