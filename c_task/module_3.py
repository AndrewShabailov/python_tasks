class Car:
    def __init__(self, color: str, price: float):
        self.color = color
        self.price = price

    def get_final_price(self) -> float:
        if self.color.lower() == 'красный':
            return self.price * 1.15
        return self.price


class NewCar(Car):
    def __init__(self, color, price, has_trailer:bool):
        super().__init__(color, price)
        self.has_trailer = has_trailer

    def get_final_price(self) -> float:
        final_price = super().get_final_price()
        if self.has_trailer:
            return final_price + self.price * 0.35
        return final_price


car1 = Car('красный', 100)
car2 = Car('зеленый', 100)
car3 = NewCar('синий', 100, False)
car4 = NewCar('красный', 100, True)



print("Машина красного цвета: ", car1.get_final_price())
print("Машина зеленого цвета: ", car2.get_final_price())
print("Машина синего цвета без прицепа: ", car3.get_final_price())
print("Машина красного цвета с прицепом: ", car4.get_final_price())
