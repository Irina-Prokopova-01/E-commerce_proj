from src.order import Order
import pytest


def test_order_init(first_product):
    order = Order(first_product, 10)
    assert order.products == "Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера"
    assert order.quantity == 10
    assert order.total_price == 1800000.0


def test_order_new_quantity(first_product):
    order = Order(first_product, 10)
    assert order.products == "Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера"
    assert order.quantity == 10
    assert order.total_price == 1800000.0
    order.quantity = 15
    assert order.products == "Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера"
    assert order.quantity == 25
    assert order.total_price == 4500000.0


def test_order_new_product(first_product):
    order = Order(first_product, 10)
    assert order.products == "Samsung Galaxy C23 Ultra, 256GB, Серый цвет, 200MP камера"
    assert order.quantity == 10
    assert order.total_price == 1800000.0
    with pytest.raises(ValueError):
        order.products = "New_product"
