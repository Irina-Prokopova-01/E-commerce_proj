def test_category_iterator(product_iterator):
    assert product_iterator.index == 0
    assert next(product_iterator).name == 'Samsung Galaxy C23 Ultra'
    assert next(product_iterator).description == 'Фоновая подсветка'
    # assert next(product_iterator).price == 180000.0
