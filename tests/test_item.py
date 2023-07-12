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


"""
Хотел сделать тест на занесение в список, но на выходе у объектов разные коды, 
поэтому на данном этапе не вижу возможности это протестировать
"""
Item("Смартфон", 10000, 20)
Item("Ноутбук", 20000, 5)
# assert Item.all == [Item("Смартфон", 10000, 20), Item("Ноутбук", 20000, 5)]
print(Item.all)
print([Item("Смартфон", 10000, 20), Item("Ноутбук", 20000, 5)])
