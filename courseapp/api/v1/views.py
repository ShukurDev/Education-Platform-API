from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from courseapp.models import CourseModel, CommentModel
from rest_framework.response import Response
from courseapp.api.v1.serializers import CourseSerializer, CourseCommentsSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import permissions

class CourseList(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer


class CourseDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer


class CourseCommentsList(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CommentModel.objects.all()
    serializer_class = CourseCommentsSerializer
