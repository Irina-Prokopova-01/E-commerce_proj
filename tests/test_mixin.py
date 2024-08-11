from src.lawnGrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_mixin(capsys):
    Product("55 QLED 4K", "Фоновая подсветка", 123000.0, 7)
    message = capsys.readouterr()
    assert message.out.strip() == "Product(55 QLED 4K, Фоновая подсветка 123000.0 7)"


def test_smartphone_mixin(capsys):
    Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    message = capsys.readouterr()
    assert message.out.strip() == "Smartphone(Iphone 15, 512GB, Gray space 210000.0 8)"


def test_lawn_grass_mixin(capsys):
    LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    message = capsys.readouterr()
    assert (
        message.out.strip()
        == "LawnGrass(Газонная трава, Элитная трава для газона 500.0 20)"
    )
