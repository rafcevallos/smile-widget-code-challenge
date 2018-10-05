from django.conf.urls import url, include
from django.urls import path
from products import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router = routers.DefaultRouter()

router.register(r'products', views.Products)
router.register(r'gift_cards', views.GiftCards)
router.register(r'get-price', views.ProductPrices)

urlpatterns = [
    url(r'^', include(router.urls)),
    url('get-price/productCode={code}&&date={date}&&giftCardCode={giftCardCode})
    # something like this
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
