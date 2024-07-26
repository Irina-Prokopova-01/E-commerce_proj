import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_product():
    return Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def second_product():
    return Product(
        name='55" QLED 4K', description="Фоновая подсветка", price=123000.0, quantity=7
    )


@pytest.fixture
def three_product():
    return Product(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def category_product_1():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций",
        products=[
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5,
            }
        ],
    )


@pytest.fixture
def category_product_2():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом",
        products=[
            {
                "name": '55" QLED 4K',
                "description": "Фоновая подсветка",
                "price": 123000.0,
                "quantity": 7,
            }
        ],
    )
