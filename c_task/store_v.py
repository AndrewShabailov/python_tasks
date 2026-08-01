from abc import ABC, abstractmethod


class Product(ABC):
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    @abstractmethod
    def get_category(self):
        pass

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_quantity(self):
        return self.__quantity


class Electronics(Product):
    def get_category(self):
        return "Электроника"


class Food(Product):
    def get_category(self):
        return "Продукты"


class Shop:
    def __init__(self):
        self.__product_list = []

    def add_product(self, product):
        self.__product_list.append(product)

    def show_products(self):
        for product in self.__product_list:
            print(f"["
                    f"{product.get_category()}"
                    f"] {product.get_name()} — {product.get_price()} руб. (в наличии: {product.get_quantity()})")

    def get_total_value(self):
        total = 0
        for product in self.__product_list:
            total += product.get_price() * product.get_quantity()
        return total


shop = Shop()
shop.add_product(Electronics("Ноутбук", 50000, 3))
shop.add_product(Electronics("Мышь", 1500, 10))
shop.add_product(Food("Хлеб", 50, 100))
shop.show_products()
print(f"Общая стоимость склада: {shop.get_total_value()} руб.")
