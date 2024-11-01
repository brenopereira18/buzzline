import pytest
from product.serializers import CategorySerializer
import uuid


@pytest.mark.django_db
class TestCategorySerializer:

    def test_valid_data(self):
        category_data = {
            "title": "Electronics",
            "slug": f"electronics-{uuid.uuid4()}",
            "description": "Electronics category",
            "active": True,
        }
        serializer = CategorySerializer(data=category_data)
        assert serializer.is_valid()
        assert serializer.validated_data["title"] == category_data["title"]
        assert serializer.validated_data["slug"] == category_data["slug"]
    
    def test_invalid_data(self):
        category_data = {
            "title": "",
            "slug": None,
            "description": "Electronics category",
            "active": True,
        }
        serializer = CategorySerializer(data=category_data)
        assert not serializer.is_valid()
        assert "title" in serializer.errors
        assert "slug" in serializer.errors