from src.product import Product


def test_first_product_init(first_product, second_product):
    assert first_product.name == "Samsung Galaxy C23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5

    assert second_product.name == "55 QLED 4K"
    assert second_product.description == "Фоновая подсветка"
    assert second_product.price == 123000.0
    assert second_product.quantity == 7


def test_product_price_0(first_product, capsys):
    first_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
    first_product.price = 10
    assert first_product.price == 10


def test_product_price_setter_1(first_product):
    first_product.price = 180000.0
    assert first_product.price == 180000.0


def test_product_price_setter_2(second_product):
    second_product.price = 123000.0
    assert second_product.price == 123000.0


def test_new_product_clss(product_dict):
    product_new_ = Product.new_product(product_dict)
    assert product_new_.name == "new_product"
    assert product_new_.description == "product fot test new_product"
    assert product_new_.price == 1.0
    assert product_new_.quantity == 10


def test_price_property_1(first_product):
    assert first_product.price == 180000.0


def test_product_str(second_product):
    assert str(second_product) == "55 QLED 4K, 123000.0 руб. Остаток: 7 шт."


def test_product_add_1_2(first_product, second_product):
    assert first_product + second_product == 1761000.0
