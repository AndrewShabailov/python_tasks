from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, username, email):
        self.__username = username
        self.__email = email

    @abstractmethod
    def get_role(self):
        pass

    def get_user_name(self):
        return self.__username

    def get_email(self):
        return self.__email


class AdminUser(User):
    def get_role(self):
        return "Администратор"


class RegularUser(User):
    def get_role(self):
        return "Пользователь"


class UserManager:
    def __init__(self):
        self.__user_list = []

    def add_user(self, user):
        self.__user_list.append(user)

    def show_users(self):
        for user in self.__user_list:
            print(f'[{user.get_role()}] {user.get_user_name()} ({user.get_email()})')

    def get_admins(self):
        admins = []
        for user in self.__user_list:
            if user.get_role() == "Администратор":
                admins.append(user)
        return admins


manager = UserManager()
manager.add_user(AdminUser("root", "root@test.com"))
manager.add_user(RegularUser("john", "john@test.com"))
manager.add_user(AdminUser("admin", "admin@test.com"))
manager.show_users()

print(f"Админов: {len(manager.get_admins())}")
