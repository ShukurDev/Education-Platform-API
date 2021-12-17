from django.urls import path
from courseapp.api.v1.views import CourseDetail, CourseList, CourseCommentsList

urlpatterns = [
    path("", CourseList.as_view()),
    path("<int:pk>/", CourseDetail.as_view()),
    path("comments/", CourseCommentsList.as_view()),
]

