def check_age(age):
    if age < 18:
        return "Несовершеннолетний"
    elif 18 <= age <= 65:
        return "Взрослый"
    else:
        return "Пенсионер"

def count_down(n):
    for i in reversed(range(1, n + 1)):
        print(i)
    print('Пуск!')


def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "Неизвестная операция"


def process_list(numbers):
    return f'Сумма: {sum(numbers)}, Макс: {max(numbers)}, Мин: {min(numbers)}'


def analyze_string(s):
    s = str(s)
    return (f'Длинна: {len(s)} \nВерхний регистр: {s.upper()} \nНаоборот: {s[::-1]}')

