from abc import ABC, abstractmethod

class Pay(ABC):
    def __init__(self, amount):
        self.__amount = amount

    @abstractmethod
    def pay(self):
        pass

    def get_amount(self):
        return self.__amount


class CardPayment(Pay):
    def pay(self):
        return f"Оплата картой: {self.get_amount()}"


class CashPayment(Pay):
    def pay(self):
        return f"Оплата наличными: {self.get_amount()}"


class PaymentProcessor:
    def __init__(self):
        self.amount_list = []

    def add_payment(self, payment):
        self.amount_list.append(payment)

    def process_all(self):
        for payment in self.amount_list:
            print(payment.pay())

processor = PaymentProcessor()
processor.add_payment(CardPayment(1500))
processor.add_payment(CardPayment(3500))
processor.add_payment(CashPayment(1500))
processor.process_all()
