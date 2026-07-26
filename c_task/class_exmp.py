class Book:

    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    def __str__(self):
        return f'{self.title} - {self.author}'


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book):
        self.__books.append(book)

    def show_books(self):
        for book in self.__books:
            print(book)


class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f'{self.title} - {self.author} (размер файла: {self.file_size} МБ)'






lib = Library()

book1 = Book("Домовенок", "М. Горин")
book2 = Ebook('Python для продолжающих', 'С. Миронов', 7)

lib.add_book(book1)
lib.add_book(book2)
lib.show_books()







