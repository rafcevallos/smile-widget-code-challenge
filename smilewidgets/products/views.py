from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from products.models import Product, GiftCard, ProductPrice
from products.serializers import ProductSerializer, GiftCardSerializer, ProductPriceSerializer

# Create your views here.

class Products(viewsets.ModelViewSet):
    """
    Endpoint that allows products to viewed and edited
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'put', 'post']


class GiftCards(viewsets.ModelViewSet):
    """
    Endpoint that allows Gift Cards to viewed and edited
    """
    queryset = GiftCard.objects.all()
    serializer_class = GiftCardSerializer
    http_method_names = ['get', 'put', 'post']


class ProductPrices(viewsets.ModelViewSet):
    """
    Endpoint that allows Product Prices to viewed and edited
    """
    queryset = ProductPrice.objects.all()
    serializer_class = ProductPriceSerializer
    http_method_names = ['get', 'put', 'post']