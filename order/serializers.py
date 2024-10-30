from rest_framework import serializers
from product.models import Product
from product.serializers import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=True)
    total = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['product', 'total']

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total