def test_user_init(category_product_1, category_product_2):
    assert category_product_1.name == "Смартфоны"
    assert (
        category_product_1.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций"
    )
    assert category_product_1.products_ == [
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    ]

    assert category_product_2.name == "Телевизоры"
    assert (
        category_product_2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом"
    )
    assert category_product_2.products_ == [
        {
            "name": '55" QLED 4K',
            "description": "Фоновая подсветка",
            "price": 123000.0,
            "quantity": 7,
        }
    ]

    assert len(category_product_1.products_) == 1

    assert category_product_1.category_count == 2
    assert category_product_2.category_count == 2

    assert category_product_1.product_count == 2
    assert category_product_2.product_count == 2

def test_category_get_product_property(first_product):
    print(first_product.new_product)
