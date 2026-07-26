class Vehicle:
    """vehicle class description"""

    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"Машина {self.brand} едет")


class Car(Vehicle):
    """car class description"""
    def open_trunk(self):
        print(f"Багажник открыт")


auto_1 = Car('Mercedes Benz')
auto_1.drive()
auto_1.open_trunk()
