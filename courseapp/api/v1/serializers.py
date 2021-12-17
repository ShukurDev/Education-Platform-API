from rest_framework import serializers
from courseapp.models import CourseModel, CommentModel


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = '__all__'


class CourseCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = "__all__"

