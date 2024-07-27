def test_first_product_init(first_product, second_product):
    assert first_product.name == "Samsung Galaxy C23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5

    assert second_product.name == "55 QLED 4K"
    assert second_product.description == "Фоновая подсветка"
    assert second_product.price == 123000.0
    assert second_product.quantity == 7


# def test_new_product_property_1(first_product):
#     product_new = Product.new_product(first_product)
#     assert product_new.name == <src.product.Product object at 0x0000026FFF5E3980>
#     assert product_new.description == <src.product.Product object at 0x0000026FFF5E3980>
#     assert product_new.price == <src.product.Product object at 0x0000026FFF5E3980>
#     assert product_new.quantity == <src.product.Product object at 0x0000026FFF5E3980>


def test_product_price_0(first_product, capsys):
    first_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_product_price_setter(first_product):
    assert first_product.price.setter == 180000.0
