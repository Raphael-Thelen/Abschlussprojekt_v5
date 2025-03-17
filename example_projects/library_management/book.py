class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_loaned = False

    def loan(self):
        self.is_loaned = True

    def return_book(self):
        self.is_loaned = False