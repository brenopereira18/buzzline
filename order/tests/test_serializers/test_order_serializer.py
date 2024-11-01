import pytest
from order.serializers import OrderSerializer
from product.models import Product, Category
from order.models import Order, User


@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", password="password")

@pytest.fixture
def category(db):
    category1 = Category.objects.create(title="Categoria 1", slug="categoria-1")
    category2 = Category.objects.create(title="Categoria 2", slug="categoria-2")
    return category1, category2

@pytest.fixture
def products(category, db):
    product1 = Product.objects.create(title="Produto 1", price=100.0)
    product1.category.add(category[0])  
    product2 = Product.objects.create(title="Produto 2", price=200.0)
    product2.category.add(category[1])  
    return product1, product2

@pytest.fixture
def order(user, products, db):
    order = Order.objects.create(user=user)
    
    # Adiciona os produtos ao pedido
    order.product.set(products)  
    return order

def test_order_serializer(order):
    serializer = OrderSerializer(order)
    
    # Verifica os dados serializados
    data = serializer.data
    assert 'product' in data
    
    # Verifica que há dois produtos
    assert len(data['product']) == 2  

    # Verifica os dados de cada produto
    assert data['product'][0]['title'] == order.product.all()[0].title
    assert data['product'][1]['title'] == order.product.all()[1].title
    
    # Verifica o campo total
    expected_total = sum(product.price for product in order.product.all())
    assert data['total'] == expected_total  
