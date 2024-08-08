import pytest


def test_smartphone_init(smartphone_1):
    assert smartphone_1.name == "Iphone 15"
    assert smartphone_1.description == "512GB, Gray space"
    assert smartphone_1.price == 210000.0
    assert smartphone_1.quantity == 8
    assert smartphone_1.efficiency == 98.2
    assert smartphone_1.model == "15"
    assert smartphone_1.color == "Gray space"
    assert smartphone_1.memory == 512


def test_smartphone_add(smartphone_1, smartphone_2):
    assert smartphone_1 + smartphone_2 == 2114000.0


def test_smartphone_add_error(smartphone_1):
    # result = task_periodic1 + 1
    with pytest.raises(TypeError):
        result = smartphone_1 + 1
