class User:

    def __init__(self, username):
        self.username = username
        self.password = None

    def set_password(self, password):
        if self.is_password_strong(password):
            self.password = password
            print(f"Пароль для пользователя {self.username} успешно установлен")
        else:
            print("Пароль слишком слабый")

    @staticmethod
    def is_password_strong(password):
       return len(password) > 6 and any(char.isdigit() for char in password)


user_1 = User('Андрей')
user_1.set_password("veryStrictPass1")
print(user_1.password)
print("---")
user_2 = User('Юра')
user_2.set_password("key")
print(user_2.password)
