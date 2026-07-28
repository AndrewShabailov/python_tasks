from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.__brand = brand

    @abstractmethod
    def move(self):
        pass

    def get_brand(self):
        return self.__brand


class Car(Vehicle):
    def move(self):
        return "Едет на бензине"


class Bicycle(Vehicle):
    def move(self):
        return "Едет на педалях"


class Fleet:
    def __init__(self):
        self.transport_list = []

    def add_vehicle(self, vehicle):
        self.transport_list.append(vehicle)

    def show_all_moves(self):
        for vehicle in self.transport_list:
            print(f"{vehicle.get_brand()}: {vehicle.move()}")



ft = Fleet()
ft.add_vehicle(Bicycle('Аист'))
ft.add_vehicle(Car('Белджи'))
ft.show_all_moves()
