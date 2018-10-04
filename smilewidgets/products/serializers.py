from rest_framework import serializers
from products.models import Product, GiftCard, ProductPrice


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'name', 'code', 'price')

class GiftCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftCard
        fields = ('pk', 'code', 'amount', 'date_start', 'date_end')

class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ('pk', 'code', 'date_start', 'date_end',)