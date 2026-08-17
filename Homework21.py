import json
from datetime import datetime


class Book:
    def __init__(self, book_id, title, author, year, is_borrowed=False):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.is_borrowed = is_borrowed

    def print_info(self):
        status = "Книга [видана]" if self.is_borrowed else "Книга [у бібліотеці]"
        print(
            f"ID: {self.id} | {self.title} | {self.author} | {self.year} {status}"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "is_borrowed": self.is_borrowed,
        }


class Library:
    def __init__(self):
        self.books = []
        self.filename = "library.json"
        self.load()

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            self.books = [
                Book(
                    item["id"],
                    item["title"],
                    item["author"],
                    item["year"],
                    item["is_borrowed"],
                )
                for item in data
            ]

        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(
                [book.to_dict() for book in self.books],
                file,
                ensure_ascii=False,
                indent=4,
            )

    def get_next_id(self):
        if not self.books:
            return 1
        return max(book.id for book in self.books) + 1

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def input_year(self):
        current_year = datetime.now().year

        while True:
            year = input("Введіть рік видання: ")

            if not year.isdigit():
                print("❌ Рік має бути числом!")
                continue

            year = int(year)

            if 1500 <= year <= current_year:
                return year

            print(f"❌ Рік має бути від 1500 до {current_year}")

    def add_book(self):
        title = input("Назва книги: ")
        author = input("Автор: ")
        year = self.input_year()

        book = Book(
            self.get_next_id(),
            title,
            author,
            year,
            False
        )

        self.books.append(book)
        self.save()

        print("✅ Книгу додано!")

    def show_books(self):
        if not self.books:
            print("📭 Бібліотека порожня.")
            return

        print("\nСортування:")
        print("1. За назвою")
        print("2. За автором")

        choice = input("Ваш вибір: ")

        if choice == "2":
            sorted_books = sorted(self.books, key=lambda x: x.author.lower())
        else:
            sorted_books = sorted(self.books, key=lambda x: x.title.lower())

        for book in sorted_books:
            book.print_info()

    def delete_book(self):
        try:
            book_id = int(input("Введіть ID книги: "))
        except ValueError:
            print("❌ ID має бути числом!")
            return

        book = self.find_book_by_id(book_id)

        if not book:
            print("❌ Книгу не знайдено.")
            return

        self.books.remove(book)
        self.save()

        print("✅ Книгу видалено.")

    def borrow_book(self):
        try:
            book_id = int(input("Введіть ID книги: "))
        except ValueError:
            print("❌ ID має бути числом!")
            return

        book = self.find_book_by_id(book_id)

        if not book:
            print("❌ Книгу не знайдено.")
            return

        if book.is_borrowed:
            print("❌ Книга вже видана.")
            return

        book.is_borrowed = True
        self.save()

        print("✅ Книгу видано читачеві.")

    def return_book(self):
        try:
            book_id = int(input("Введіть ID книги: "))
        except ValueError:
            print("❌ ID має бути числом!")
            return

        book = self.find_book_by_id(book_id)

        if not book:
            print("❌ Книгу не знайдено.")
            return

        if not book.is_borrowed:
            print("❌ Книга вже знаходиться у бібліотеці.")
            return

        book.is_borrowed = False
        self.save()

        print(" Книгу повернуто.")

    def find_by_author(self):
        author = input("Введіть автора: ").lower()

        found = [
            book for book in self.books
            if author in book.author.lower()
        ]

        if not found:
            print("📭 Книг не знайдено.")
            return

        for book in found:
            book.print_info()

    def find_by_keyword(self):
        keyword = input("Введіть ключове слово: ").lower()

        found = [
            book for book in self.books
            if keyword in book.title.lower()
        ]

        if not found:
            print("📭 Книг не знайдено.")
            return

        for book in found:
            book.print_info()

    def run(self):
        while True:
            print("\n--- Бібліотека ---")
            print("1. Додати книгу")
            print("2. Переглянути всі книги")
            print("3. Видалити книгу")
            print("4. Видати книгу")
            print("5. Повернути книгу")
            print("6. Пошук за автором")
            print("7. Пошук за ключовим словом")
            print("8. Вийти")

            choice = input("Оберіть пункт: ")

            if choice == "1":
                self.add_book()

            elif choice == "2":
                self.show_books()

            elif choice == "3":
                self.delete_book()

            elif choice == "4":
                self.borrow_book()

            elif choice == "5":
                self.return_book()

            elif choice == "6":
                self.find_by_author()

            elif choice == "7":
                self.find_by_keyword()

            elif choice == "8":
                print("До побачення!")
                break

            else:
                print("Невірний вибір.")


library = Library()
library.run()