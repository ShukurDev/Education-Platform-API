from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('profileapp.api.v1.urls')),
]