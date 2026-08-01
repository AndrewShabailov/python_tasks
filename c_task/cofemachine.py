from abc import ABC, abstractmethod


class Drink(ABC):
    def __init__(self, name, volume):
        self.__name = name
        self.__volume = volume

    @abstractmethod
    def prepare(self):
        pass

    def get_name(self):
        return self.__name

    def get_volume(self):
        return self.__volume


class Coffee(Drink):
    def prepare(self):
        return f"Варю кофе {self.get_name()} объёмом {self.get_volume()}мл"


class Tea(Drink):
    def prepare(self):
        return f"Завариваю чай {self.get_name()} объёмом {self.get_volume()} мл"


class CoffeeMachine:
    def __init__(self):
        self.__menu = []

    def add_drink(self, drink):
        self.__menu.append(drink)

    def show_menu(self):
        for menu in self.__menu:
            menu.prepare()

    def get_drink_count(self):
        count = 0
        for drink in self.__menu:
            count += 1
            print(drink.prepare())
        return count


machine = CoffeeMachine()
machine.add_drink(Coffee("Эспрессо", 50))
machine.add_drink(Coffee("Латте", 300))
machine.add_drink(Tea("Зелёный", 200))
machine.show_menu()

print(f"Напитков в меню: {machine.get_drink_count()}")
