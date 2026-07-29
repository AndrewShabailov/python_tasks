from abc import ABC, abstractmethod


class Test(ABC):
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def run(self):
        pass

    def get_name(self):
        return self.__name


class UnitTest(Test):
    def run(self):
        return "Запускаю юнит-тест"


class IntegrationTest(Test):
    def run(self):
        return "Запускаю интеграционный тест"


class TestSuite:
    def __init__(self):
        self.test_suite = []

    def add_test(self, test):
        self.test_suite.append(test)

    def run_all(self):
        for test in self.test_suite:
            print(f"[Тест] {test.get_name()}: {test.run()}")


suite = TestSuite()
suite.add_test(UnitTest("Проверка логина"))
suite.add_test(IntegrationTest("Проверка API"))
suite.run_all()
