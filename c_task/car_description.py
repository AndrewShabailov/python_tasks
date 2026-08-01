class Car:
    def __init__(self, color, price):
        self._color = color
        self.price = price

    def get_final_price(self):
        color = self._color
        if color == "red":
            return self.price * 1.15
        else:
            return self.price


class NewCar(Car):
    def __init__(self, color, price, trailer):
        super().__init__(color, price)
        self.has_trailer = trailer

    def get_final_price(self):
        base_price = super().get_final_price()

        if self.has_trailer:
            base_price += self.price * 0.35
        return int(base_price)


car1 = NewCar("red", 100, trailer=True)
car2 = Car("blue", 200)

print(car1.get_final_price())
print(car2.get_final_price())
