from contextlib import contextmanager

@contextmanager
def simple_counter():
    print("Начало блока")
    try:
        yield
    finally:
        print("Конец блока")

with simple_counter():
    print("Работаем внутри")
