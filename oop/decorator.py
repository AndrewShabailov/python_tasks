def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Вызвана функция {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@log_calls
def add(x, y):
    print(x + y)

@log_calls
def greet(name):
    print(f"Привет, {name}")


add(2,3)
greet("Питон")
