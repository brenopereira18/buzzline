import pytest
from product.serializers import ProductSerializer
from product.models import Category
import uuid


@pytest.mark.django_db
class TestProductSerializer:
    
    def test_valid_data(self):             
        
        product_data = {
            "title": "Smartphone",
            "description": "Latest model smartphone",
            "price": 999,
            "active": True,
            "category": [
                {"title": "Electronics", "slug": f"electronics-{str(uuid.uuid4())[:8]}", "description": "Category for electronics", "active": True},
                {"title": "Home Appliances", "slug": f"home-appliances-{str(uuid.uuid4())[:8]}", "description": "Category for home appliances", "active": True}
            ],
        }
        serializer = ProductSerializer(data=product_data)
        is_valid = serializer.is_valid()
        print("Validation Result:", is_valid)
        print("Errors:", serializer.errors)
        assert serializer.is_valid()  

    def test_invalid_data(self):
        product_data = {
            "title": "Smartphone",
            "description": "Latest model smartphone",
            "price": -100,
            "active": True,
            "category": [],  
        }
        serializer = ProductSerializer(data=product_data)
        assert not serializer.is_valid()
        assert "price" in serializer.errors
        