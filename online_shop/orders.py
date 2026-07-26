class PaymentMethod:
    def pay(self, order):
        raise NotImplementedError

class CashPayment(PaymentMethod):
    def pay(self, order):
        print(f"Оплата наличными: {order.total} руб.")

class CardPayment(PaymentMethod):
    def pay(self, order):
        print(f"Оплата картой: {order.total} руб.")

class PayPalPayment(PaymentMethod):
    def pay(self, order):
        print(f"Оплата через Paypal: {order.total} руб.")


class Order:
    def __init__(self, items: list, total: float):
        self.items = items
        self.total = total

    def get_info(self):
        items_str = " ,".join(self.items)
        return f"заказ: [{items_str}], сумма: {self.total} руб."


class OrderProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process(self, order: Order):
        print(f"Обрабатываем {order.get_info()}")
        self.payment_method.pay(order)


order = Order(['Книга', 'Ручка'], 100)

cash = OrderProcessor(CashPayment())
card = OrderProcessor(CardPayment())
paypal = OrderProcessor(PayPalPayment())

cash.process(order)
card.process(order)
paypal.process(order)
