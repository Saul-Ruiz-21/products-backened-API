from django.shortcuts import get_object_or_404
from urllib import response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from product import serializers

@api_view(['GET', 'POST'])
def product_list(request):

    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)