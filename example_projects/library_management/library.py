from book import Book
from user import User
from loan import Loan
import database

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.loans = []

    def add_book(self, title, author):
        book_id = len(self.books) + 1
        book = Book(book_id, title, author)
        self.books.append(book)
        print("Buch hinzugefügt.")

    def add_user(self, name):
        user_id = len(self.users) + 1
        user = User(user_id, name)
        self.users.append(user)
        print("Benutzer hinzugefügt.")

    def loan_book(self, user_id, book_id):
        user = next((u for u in self.users if u.user_id == int(user_id)), None)
        book = next((b for b in self.books if b.book_id == int(book_id)), None)
        if user and book and not book.is_loaned:
            book.loan()
            loan = Loan(user, book)
            self.loans.append(loan)
            print("Buch ausgeliehen.")
        else:
            print("Ausleihe nicht möglich.")

    def return_book(self, book_id):
        book = next((b for b in self.books if b.book_id == int(book_id)), None)
        if book and book.is_loaned:
            book.return_book()
            print("Buch zurückgegeben.")
        else:
            print("Buch nicht ausgeliehen.")

    def load_data(self):
        self.books = database.load_books()
        self.users = database.load_users()

    def save_data(self):
        database.save_books(self.books)
        database.save_users(self.users)