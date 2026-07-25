class BookStore:
    """books description class"""
    books_count = 0                 # class attribute

    def __init__(self, title, price):
        self.title = title           # instance attributes
        self.price = price
        BookStore.books_count += 1

    def get_info(self):
        return f"Название книги: {self.title}, цена: {self.price}"

    @classmethod
    def total_books(cls):
        print(f"Всего книг в магазине: {cls.books_count}")

    @classmethod
    def from_string(cls, data):
        title, price = data.split(",")
        return cls(title.strip(), int(price.strip()))

    @staticmethod
    def is_valid_price(price):
        return f"{price > 0}"


book1 = BookStore("Гарри Поттер", "100")
book2 = BookStore.from_string("Властелин колец, 300")

print(book1.get_info())
BookStore.total_books()
print(book2.is_valid_price(10))
