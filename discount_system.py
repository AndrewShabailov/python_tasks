from abc import ABC, abstractmethod


class Discount(ABC):
    def __init__(self, name, percent):
        self.__name = name
        self.__percent = percent

    @abstractmethod
    def apply(self, price):
        return price * self.__percent

    def get_name(self):
        return self.__name

    def get_percent(self):
        return self.__percent


class SaleDiscount(Discount):
    def apply(self, price):
        return f"Распродажа ({self.get_percent()}): {price - (price * self.get_percent() / 100)} руб."


class PromoDiscount(Discount):
    def apply(self, price):
        return f"Промокод ({self.get_percent()}): {price - (price * self.get_percent() / 100)} руб."


class DiscountService:
    def __init__(self):
        self.discount_list = []

    def add_discount(self, discount):
        self.discount_list.append(discount)

    def apply_all(self, price):
        for discount in self.discount_list:
            print(discount.apply(price))


service = DiscountService()
service.add_discount(SaleDiscount("Летняя", 20))
service.add_discount(PromoDiscount("SUMMER10", 10))
service.apply_all(1000)
