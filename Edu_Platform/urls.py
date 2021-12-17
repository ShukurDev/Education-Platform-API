from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions # new
from drf_yasg.views import get_schema_view # new
from drf_yasg import openapi # new
schema_view = get_schema_view( # new
    openapi.Info(
        title="Education API",
        default_version="v1",
        description="The best of Education Platform for learning programming",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="shukurdev02@gmail.com"),
        license=openapi.License(name="Not License"),
        ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.api.urls')),
    path('courses/', include('courseapp.api.urls')),
    path('orders/', include('orderapp.api.urls')),
    path('profile/', include('profileapp.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path('swagger/', schema_view.with_ui( # new
        'swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui( # new
        'redoc', cache_timeout=0), name='schema-redoc'),
]