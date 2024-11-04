from rest_framework import serializers
from product.models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = [
            'title',
            'slug',
            'description',
            'active',
        ]
        

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True, many=True,)
    categories_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, many=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'price',
            'active',
            'category',
            'categories_id',
        ]

    def create(self, validade_data):
        category_data = validade_data.pop('categories_id')

        product = Product.objects.create(**validade_data)
        for category in category_data:
            product.category.add(category)

        return product