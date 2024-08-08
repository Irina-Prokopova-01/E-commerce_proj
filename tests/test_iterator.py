import pytest


def test_category_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy C23 Ultra"
    assert next(product_iterator).description == "Фоновая подсветка"

    with pytest.raises(StopIteration):
        next(product_iterator)


def test_category_iterator2(product_iterator):
    assert next(product_iterator).quantity == 5
    assert next(product_iterator).price == 123000
