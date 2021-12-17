from django.urls import path

from orderapp.api.v1.views import OrderList, OrderDetail

urlpatterns = [
    path("", OrderList.as_view()),
    path("<int:pk>/", OrderDetail.as_view()),
]