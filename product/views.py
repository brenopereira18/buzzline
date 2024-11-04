from rest_framework.viewsets import ModelViewSet
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()
    

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()
