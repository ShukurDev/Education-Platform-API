from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from orderapp.models import OrderModel
from orderapp.api.v1.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated,IsAdminUser

class OrderList(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer



class OrderDetail(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
