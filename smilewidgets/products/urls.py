from django.conf.urls import url, include
from products import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter


router = routers.DefaultRouter()

router.register(r'products', views.Products)
router.register(r'gift_cards', views.GiftCards)
router.register(r'product_prices', views.ProductPrices)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]