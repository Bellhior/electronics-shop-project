import pytest

from src.item import Item


@pytest.fixture
def item_1():
    return Item("Смартфон", 10500, 20)


@pytest.fixture
def item_2():
    return Item("Ноутбук", 28000, 5)
