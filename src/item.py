import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @classmethod
    def instantiate_from_csv(cls):
        """
           Класс-метод, инициализирующий экземпляры класса `Item`
           данными из файла src/items.csv
        """
        csv_import = os.path.join(os.path.dirname(__file__), "items.csv")
        cls.all.clear()
        with open(csv_import, newline='') as csvfile:  # encoding='windows-1251', у меня корректно изначально
            reader = csv.DictReader(csvfile)
            thing: dict
            for thing in reader:
                name = thing['name']
                price = cls.string_to_number(thing['price'])
                quantity = cls.string_to_number(thing['quantity'])
                cls(name, price, quantity)

    @property
    def name(self) -> str:
        """Получает название товара"""
        return self.__name

    @name.setter
    def name(self, new_name) -> None:
        """Показывает первые 10 символов в названии"""
        # if len(new_name) > 10: - можно вызвать ошибку
        # raise Exception("Длина наименования товара превышает 10 символов.")
        self.__name = new_name[:10]

    @staticmethod
    def string_to_number(string: str) -> int:
        """Возвращает число из числа-строки"""
        # if string[0].isdigit():
        if string.replace(".", "").isdigit():
            return int(float(string))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price
