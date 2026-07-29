from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    @abstractmethod
    def read(self):
        pass

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author


class EBook(Book):
    def read(self):
        return "Читаю электронную книгу"


class PaperBook(Book):
    def read(self):
        return "Листаю бумажную книгу"


class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)

    def show_books(self):
        for book in self.book_list:
            print(f"{book.get_author()} - {book.get_title()}: {book.read()}")


library = Library()
library.add_book(EBook("Чистый код", "Мартин"))
library.add_book(PaperBook("Автостопом по галактике", "Адамс"))
library.show_books()
