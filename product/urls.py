from django.urls import path, include
from rest_framework import routers
from product import views

router = routers.SimpleRouter()
router.register(r'product', views.ProductViewSet, basename='product')


urlpatterns = [
    path('', include(router.urls))
]