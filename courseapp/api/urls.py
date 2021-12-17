from django.urls import path,include

urlpatterns = [
    path('api/v1/', include('courseapp.api.v1.urls')),
]