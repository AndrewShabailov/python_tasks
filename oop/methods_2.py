class BankAccount:

    bank_name = "Сбербанк"

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if self.is_amount_valid(amount):
            self.balance += amount
            print(f"{self.owner} пополнил(-а) счет на {amount}. Баланс: {self.balance + amount}")
        else:
            print(f"Сумма должна быть больше 0")

    def withdraw(self, amount):
        if not self.is_amount_valid(amount):
            print(f"Сумма должна быть больше 0")
        elif amount < self.balance:
            print(f"Недостаточно средств")
        else:
            self.balance -= amount
            print(f"{self.owner} снял(-а) {amount}. Баланс {self.balance}")

    @classmethod
    def bank_info(cls):
        return f"Добро пожаловать в {cls.bank_name}"

    @staticmethod
    def is_amount_valid(amount):
        return amount > 0


acc_1 = BankAccount('Андрей', 100)
print(acc_1.bank_info())

acc_1.deposit(100)
acc_1.withdraw(100)
acc_1.withdraw(200)
print(BankAccount.is_amount_valid(100))
