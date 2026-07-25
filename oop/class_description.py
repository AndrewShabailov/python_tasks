class DogClass:
    """dog description class"""
    species = "собака"

    def __init__(self, name, age):
        """dogs attribute"""
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} лает: Гав!")


kind_dog = DogClass('Добрая собака', 5)
angry_dog = DogClass('Злая собака', 3)

print(f"{kind_dog.name}, возраст: {kind_dog.age}, вид: {kind_dog.species}")
kind_dog.bark()

print(f"{angry_dog.name}, возраст: {angry_dog.age}, вид: {angry_dog.species}")
angry_dog.bark()
