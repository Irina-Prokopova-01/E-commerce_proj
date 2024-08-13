import pytest


def test_user_init(category_product_1, category_product_2):
    assert category_product_1.name == "Смартфоны"
    assert (
        category_product_1.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций"
    )
    assert (
        category_product_1.products
        == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "55 QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"
    )

    assert category_product_2.name == "Телевизоры"
    assert (
        category_product_2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом"
    )
    assert (
        category_product_2.products
        == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "55 QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"
    )

    assert len(category_product_1.products_list) == 2

    assert category_product_1.category_count == 2
    assert category_product_2.category_count == 2

    assert category_product_1.product_count == 4
    assert category_product_2.product_count == 4


# def test_products_list_property_1(category_product_1):
#     assert category_product_1.products_list == [
#         {
#             "description": "256GB, Серый цвет, 200MP камера",
#             "name": "Samsung Galaxy C23 Ultra",
#             "price": 180000.0,
#             "quantity": 5,
#         }
#     ]


# def test_get_product_property_2(category_product_2):
#     assert category_product_2.add_product == '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.'


def test_products_list_property_2(category_product_2):
    assert (
        category_product_2.products_list[-1]
        == "Product(55 QLED 4K, Фоновая подсветка 123000.0 7)"
    )


def test_add_product(category_product_1, three_product):
    category_product_1.add_product(three_product)
    # len(category_product_1.products_list) == 1
    for product in category_product_1.products_list:
        assert three_product.name == "Смартфоны"
        assert three_product.price == 180000.0
        assert three_product.quantity == 5


def test_products_property_(category_product_2):
    assert (
        category_product_2.products
        == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n55 QLED 4K, 123000.0 руб. Остаток: 7 шт.\n"
    )


def test_category_str(category_product_2):
    assert str(category_product_2) == "Телевизоры, количество продуктов: 2 шт."


def test_add_category_not_product(category_product_1, fake_product):
    with pytest.raises(TypeError):
        category_product_1.add_product(fake_product)


def test_middel_price(category_product_2, category_without_products):
    assert category_product_2.middle_price() == 146750.0
    assert category_without_products.middle_price() == 0
