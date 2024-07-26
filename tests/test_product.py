from src.product import Product

def test_first_product_init(first_product, second_product):
    assert first_product.name == "Samsung Galaxy C23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5

    assert second_product.name == '55" QLED 4K'
    assert second_product.description == "Фоновая подсветка"
    assert second_product.price == 123000.0
    assert second_product.quantity == 7


def test_new_product_property_1(first_product):
    assert first_product.new_product == 'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.'


