class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def get_name(self):
        return self.name

    def get_sound(self):
        return self.sound

    def speak(self):
        return f"{self.get_name()} говорит {self.get_sound()}"


class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)  # ← ключевое исправление
        self.breed = breed

    def get_breed(self):
        return self.breed

    def speak(self):
        parent_speech = super().speak()
        return f"{parent_speech}\n{self.breed}: Хвост виляет!"


d1 = Animal('пес', 'рычит')
d2 = Animal('Жук', 'жжж')
d3 = Dog('Шарик', 'гав', 'Бульдог')


print(d1.speak())
print(d2.speak())
print(d3.speak())
