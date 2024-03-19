from django.shortcuts import render
from rest_framework import viewsets
from .models import MainCategory, SubCategory, SubTypeCategory, Product, Cart, Checkout
from .serializers import ProductSerializer, MainSerializer, SubSerializer, SubTypeSerializer, CheckoutSerializer, CartSerializer
from rest_framework.views import APIView
from rest_framework.response import Response



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Show_main_category(APIView):
    def get(self, request):
        queryset = MainCategory.objects.all()
        serializer = MainSerializer(queryset, many=True).data
        return Response(serializer)
    
    def post(self, request):
        data = request.data
        serializer = MainSerializer(data=data).data
        if serializer.is_valid():
            serializer.save
            return Response(serializer)
        
        return Response(serializer.errors)

class NewArrivals(APIView):
    def get(self, request):
        queryset = Product.objects.order_by('-created_at', '-updated_at')
        serializer = SubSerializer(queryset, many=True).data
        
        return Response(serializer)