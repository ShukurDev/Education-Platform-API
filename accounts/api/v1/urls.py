from django.urls import path

from accounts.api.v1.views import AccountsList,AccountsDetail

urlpatterns = [
    path("", AccountsList.as_view()),
    path("<int:pk>/", AccountsDetail.as_view()),
]
