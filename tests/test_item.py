from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""


# TestCase1
def test_item(item_1, item_2):
    assert item_1.name == "Смартфон"
    assert item_1.price == 10500
    assert item_1.quantity == 20
    assert item_2.name == "Ноутбук"
    assert item_2.price == 28000
    assert item_2.quantity == 5


# TestCase2
def test_calculate_total_price(item_1, item_2):
    assert item_1.calculate_total_price() == 210000
    assert item_2.calculate_total_price() == 140000


# TestCase3
def test_apply_discount(item_1, item_2):
    Item.pay_rate = 0.5
    assert item_1.apply_discount() == 5250.0
    assert item_2.apply_discount() == 14000.0


# TestCase4
def test_add_to_list():
    """Проверка на добавление в список all"""
    Item.all = []
    item_3 = Item('Планшет', 15000, 35)
    assert len(item_3.all) == 1
    assert isinstance(Item.all[0], Item)
    item_4 = Item('Флешка', 500, 40)
    assert len(item_4.all) == 2
    assert isinstance(item_4.all[1], Item)


# TestCase5
def test_name(item_2):
    assert item_2.name == "Ноутбук"
# длина наименования товара больше 10 символов
    item_2.name = "МощныйНоутбук"
    assert item_2.name == "МощныйНоут"


# TestCase6
def test_instantiate_from_csv():
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам
    item1 = Item.all[1]
    assert item1.name == 'Ноутбук'
    item2 = Item.all[4]
    assert item2.price == 75
    item3 = Item.all[0]
    assert item3.quantity == 1


# TestCase7
def test_string_to_number():
    assert Item.string_to_number('55') == 55
    assert Item.string_to_number('45.0') == 45
    assert Item.string_to_number('3.53452352') == 3
