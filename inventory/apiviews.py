from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from inventory.models import Product, Batch, Order
from  inventory.serializers import ProductSerializer, BatchSerializer, OrderSerializer

from datetime import date
import datetime


# Lists all products and creates product instances
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Retrieves, updates and deletes product instances
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Lists all batches and creates batch instances
class BatchList(generics.ListCreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer


# Retrieves, updates and deletes batch instances
class BatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer


# Retrieves expired products  
class ExpiredProducts(generics.ListAPIView):
    queryset = Batch.objects.filter(expiry_date__lt=date.today())
    serializer_class = BatchSerializer

# Retrieves fresh products ie. products who expire in more then 3 days from today
class FreshProducts(generics.ListAPIView):
    queryset = Batch.objects.filter(expiry_date__gt=date.today()+datetime.timedelta(days=3))
    serializer_class = BatchSerializer

# Retrieves expiring products ie. products who expire in three days
class ExpiringProducts(generics.ListAPIView):
    queryset = Batch.objects.filter(expiry_date__lte=date.today()+datetime.timedelta(days=3)).exclude(expiry_date__lt=date.today())
    serializer_class = BatchSerializer

# Lists all orders and creates order instances
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# decrease the batch size when saving the model