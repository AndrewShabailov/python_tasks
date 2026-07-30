from abc import ABC, abstractmethod


class Logger(ABC):
    def __init__(self, log_name):
        self.__log_name = log_name

    @abstractmethod
    def log(self, message):
        pass

    def get_log_name(self):
        return self.__log_name


class FileLogger(Logger):
    def log(self, message):
        return f'[FILE]{self.get_log_name()}: {message}'


class ConsoleLogger(Logger):
    def log(self, message):
        return f'[Console]{self.get_log_name()}: {message}'

class LogManager:
    def __init__(self):
        self.__logger_list = []

    def add_logger(self, logger):
        self.__logger_list.append(logger)

    def log_all(self, message):
        for logger in self.__logger_list:
            print(logger.log(message))


manager = LogManager()
manager.add_logger(FileLogger("app.log"))
manager.add_logger(ConsoleLogger("debug"))
manager.log_all("Тест запущен")
