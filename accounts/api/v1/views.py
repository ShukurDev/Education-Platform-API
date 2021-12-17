from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from accounts.models import User
from accounts.api.v1.serializers import AccountsSerializer
from rest_framework import permissions

class AccountsList(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = AccountsSerializer


class AccountsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = User.objects.all()
    serializer_class = AccountsSerializer
