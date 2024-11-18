from rest_framework.viewsets import ModelViewSet
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication ]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')
    

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all().order_by('id')
