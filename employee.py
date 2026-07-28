from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        return "Пишет код"


class Tester(Employee):
    def work(self):
        return "Тестирует приложение"


class Team:
    def __init__(self):
        self.team_list = []

    def add_member(self, employee):
        self.team_list.append(employee)

    def show_work(self):
        for employee in self.team_list:
            print(f"{employee.get_name()}: {employee.work()}")


team = Team()
team.add_member(Developer("Алексей"))
team.add_member(Tester("Мария"))
team.show_work()
