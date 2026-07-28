from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def make_sound(self):
        pass

    def get_name(self):
        return self.__name

class Lion(Animal):
    def make_sound(self):
        return "Рррр!"


class Parrot(Animal):
    def make_sound(self):
        return "Привет!"


class Zoo:
    def __init__(self):
        self._z = []

    def add_animal(self, animal):
        self._z.append(animal)

    def show_all_sounds(self):
        for animal in self._z:
            print(f"{animal.get_name()} говорит {animal.make_sound()}")


zoo = Zoo()
zoo.add_animal(Lion("Симба"))
zoo.add_animal(Parrot("Кеша"))
zoo.show_all_sounds()
