from django.urls import path

from profileapp.api.v1.views import StudentsList, StudentsDetail, TeachersList, TeachersDetail

urlpatterns = [
    path("students/", StudentsList.as_view()),
    path("students/<int:pk>/", StudentsDetail.as_view()),
    path("teachers/", TeachersList.as_view()),
    path("teachers/<int:pk>/", TeachersDetail.as_view()),
]
