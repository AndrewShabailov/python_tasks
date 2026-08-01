from abc import ABC, abstractmethod

class Delivery(ABC):
    def __init__(self, item, address):
        self.__item = item
        self.__address = address

    @abstractmethod
    def deliver(self):
        pass

    def get_item(self):
        return self.__item

    def get_address(self):
        return self.__address


class CourierDelivery(Delivery):
    def deliver(self):
        return f"Курьер везет {self.get_item()} по адресу: {self.get_address()}"


class PostDelivery(Delivery):
    def deliver(self):
        return f"Почта отправляет {self.get_item()} по адресу: {self.get_address()}"


class DeliveryService:
    def __init__(self):
        self.__deliveries = []

    def add_delivery(self, delivery):
        self.__deliveries.append(delivery)

    def process_deliveries(self):
        for delivery in self.__deliveries:
            print(delivery.deliver())


service = DeliveryService()
service.add_delivery(CourierDelivery("Ноутбук", "ул. Ленина 5"))
service.add_delivery(PostDelivery("Книга", "ул. Мира 12"))
service.process_deliveries()
