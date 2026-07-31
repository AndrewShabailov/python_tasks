class Car:
    def __init__(self, color, price):
        self.color = color
        self.price = price

    def get_final_price(self):
        if self.color == 'red':
            return f'Цена машины красного цвета {int(self.price * 1.15)}'
        else:
            return f'Цена машины: {int(self.price)}'


class NewCar(Car):
    def __init__(self, price, has_trailer):
        self.price = price
        self.has_trailer = has_trailer


    def get_final_price(self):
        if self.has_trailer:
            final_price = (self.price * 1.15) + (self.price * 0.35)
            return f"Цена машины с трейлером: {int(final_price)}"
        else:
            return f'Цена машины: {int(self.price)}'


car1 = Car('red', 100)
car2 = Car('green', 100)
car3 = NewCar(100, True)
car4 = NewCar(100, False)


print(car1.get_final_price())
print(car2.get_final_price())
print(car3.get_final_price())
print(car4.get_final_price())
