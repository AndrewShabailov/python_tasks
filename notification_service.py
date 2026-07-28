from abc import ABC, abstractmethod

class Notification(ABC):

    def __init__(self, message):
        self.__message = message

    @abstractmethod
    def send(self):
        pass

    def get_message(self):
        return self.__message


class EmailNotification(Notification):

    def send(self):
        return f"Отправка Email: {self.get_message()}"


class SMSNotification(Notification):
    def send(self):
        return f"Отправка SMS: {self.get_message()}"


class NotificationService:
    def __init__(self):
        self.notify_list = []

    def add_notification(self, notification):
        self.notify_list.append(notification)

    def send_all(self):
        for notification in self.notify_list:
            print(notification.send())


service = NotificationService()
service.add_notification(EmailNotification("Ваш заказ подтверждён"))
service.add_notification(SMSNotification("Код подтверждения: 1234"))
service.send_all()
