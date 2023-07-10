from src.item import Item
""" 
В последней строке выдаёт 
[<src.item.Item object at 0x00000274AE4DEF10>, <src.item.Item object at 0x00000274AE4DF2D0>]
так как Item был импортирован, если бы он находился в этом файле, то выдалось бы как написано
внизу с __main__
"""

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    print(item1.calculate_total_price())  # 200000
    print(item2.calculate_total_price())  # 100000

    # устанавливаем новый уровень цен
    Item.pay_rate = 0.8
    # применяем скидку
    item1.apply_discount()

    print(item1.price)  # 8000.0
    print(item2.price)  # 20000

    print(Item.all)  # [<__main__.Item object at 0x000001EC6250C690>, <__main__.Item object at 0x000001EC6250C6D0>]
