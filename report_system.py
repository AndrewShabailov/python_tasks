from abc import ABC, abstractmethod


class Report(ABC):
    def __init__(self, title, data):
        self.__title = title
        self.__data = data

    @abstractmethod
    def generate(self):
        pass

    def get_title(self):
        return self.__title

    def get_data(self):
        return self.__data


class HTMLReport(Report):
    def generate(self):
        return f"HTML отчет {self.get_title()}: {self.get_data()}"


class CSVReport(Report):
    def generate(self):
        return f"CSV отчет {self.get_title()}: {self.get_data()}"


class ReportManager:
    def __init__(self):
        self.__report_list = []

    def add_report(self, report):
        self.__report_list.append(report)

    def generate_all(self):
        for i in self.__report_list:
            print(i.generate())


manager = ReportManager()
manager.add_report(HTMLReport("Продажи", [100, 200, 300]))
manager.add_report(CSVReport("Клиенты", ["Иван", "Мария", "Пётр"]))
manager.generate_all()
