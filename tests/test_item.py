from src.item import Item

"""Здесь надо написать тесты с использованием pytest для модуля item."""


# TestCase1
def test_calculate_total_price():
    assert Item.calculate_total_price(Item("Смартфон", 10000, 20)) == 200000
    assert Item.calculate_total_price(Item("Ноутбук", 20000, 5)) == 100000


# TestCase2
def test_apply_discount():
    Item.pay_rate = 0.8
    assert Item("Смартфон", 10000, 20).price*Item("Смартфон", 10000, 20).pay_rate == 8000.0
    assert Item("Ноутбук", 20000, 5).price*Item("Ноутбук", 20000, 5).pay_rate == 16000.0


# TestCase3
def test_name():
    item2 = Item('Монитор', 20000, 2)

# длина наименования товара меньше 10 символов
    assert item2.name == 'Монитор'

# длина наименования товара больше 10 символов
    item2.name = 'МониторМощный'
    assert item2.name == 'МониторМощ'


# TestCase4
def test_instantiate_from_csv():
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам
    item1 = Item.all[1]
    assert item1.name == 'Ноутбук'
    item2 = Item.all[4]
    assert item2.price == 75
    item3 = Item.all[0]
    assert item3.quantity == 1


# TestCase5
def test_string_to_number():
    assert Item.string_to_number('55') == 55
    assert Item.string_to_number('45.0') == 45
    assert Item.string_to_number('3.53452352') == 3


"""
Хотел сделать тест на занесение в список, но на выходе у объектов разные коды, 
поэтому на данном этапе не вижу возможности это протестировать
"""
Item("Смартфон", 10000, 20)
Item("Ноутбук", 20000, 5)
# assert Item.all == [Item("Смартфон", 10000, 20), Item("Ноутбук", 20000, 5)]
print(Item.all)
print([Item("Смартфон", 10000, 20), Item("Ноутбук", 20000, 5)])
