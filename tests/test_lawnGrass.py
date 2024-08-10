import pytest


def test_lawnGrass_init(lanwgrass_1):
    assert lanwgrass_1.name == "Газонная трава 2"
    assert lanwgrass_1.description == "Выносливая трава"
    assert lanwgrass_1.price == 450.0
    assert lanwgrass_1.quantity == 15
    assert lanwgrass_1.country == "США"
    assert lanwgrass_1.germination_period == "5 дней"
    assert lanwgrass_1.color == "Темно-зеленый"


def test_lawnGrass_add(lanwgrass_1, lanwgrass_2):
    assert lanwgrass_1 + lanwgrass_2 == 16750.0


def test_lawnGrass_add_error(lanwgrass_1):
    # result = task_periodic1 + 1
    with pytest.raises(TypeError):
        result = lanwgrass_1 + 1
