from django.urls import path,include

urlpatterns = [
    path('api/v1/', include('orderapp.api.v1.urls')),
]