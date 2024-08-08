import pytest

from src.category import Category
from src.iterator import Iterator
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
        name="55 QLED 4K", description="Фоновая подсветка", price=123000.0, quantity=7
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
def category_product_1(first_product, second_product):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций",
        products=[first_product, second_product],
    )


@pytest.fixture
def category_product_2(first_product, second_product):
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом",
        products=[first_product, second_product],
    )


@pytest.fixture
def product_dict():
    return {
        "name": "new_product",
        "description": "product fot test new_product",
        "price": 1.0,
        "quantity": 10,
    }


@pytest.fixture
def product_str_fixt():
    return Product(
        name="Холодильник", description="Холодильник LG", price=30000, quantity=5
    )


@pytest.fixture
def product_iterator(category_product_2):
    return Iterator(category_product_2)
