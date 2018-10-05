from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError, Http404, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.forms.models import model_to_dict
from products.models import Product, GiftCard, ProductPrice
from products.serializers import ProductSerializer, GiftCardSerializer, ProductPriceSerializer
import json
import datetime


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
    queryset = ProductPrice.objects.all
    serializer_class = ProductPriceSerializer
    http_method_names = ['get', 'put', 'post']

    # Thought process...
    # if product = 'big_widget' -- get this id -- && if dates are 11/23-11/25 -- return $800 etc
    # else if year is 2019 return $1200...but do we even need this here when they're just asking for the end point?  Shouldn't the request just return what's in the database?

    # I haven't done many conditional statements in Python/Django.  I'm not even sure if it's supposed to be in views or the serializer.

    # Also, I'm not too familiar with functional views in Django Rest since I've only made a REST API with primarily class based views.


    # I know this is what the request would look like if the end point accepts the parameters
   127.0.0.1:8000/products/get-price/productCode={code}&&date={date}&&giftCardCode={giftCardCode}