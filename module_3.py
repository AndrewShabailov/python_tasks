class Car:
    def __init__(self, color, price):
        self.color = color
        self.price = price

    def get_final_price(self):
        if self.color == 'красный':
            return int(self.price * 1.15)
        else:
            return int(self.price)


class NewCar(Car):
    def __init__(self, color, price, has_trailer):
        super().__init__(color, price)
        self.has_trailer = has_trailer

    def get_final_price(self):
        base = super().get_final_price()
        if self.has_trailer:
            return int(base + self.price * 0.35)
        return int(base)


car1 = Car('красный', 100)
car2 = Car('зеленый', 100)
car3 = NewCar('синий', 100, False)
car4 = NewCar('красный', 100, True)



print("Машина красного цвета: ", car1.get_final_price())
print("Машина зеленого цвета: ", car2.get_final_price())
print("Машина синего цвета без прицепа: ", car3.get_final_price())
print("Машина красного цвета с прицепом: ", car4.get_final_price())
