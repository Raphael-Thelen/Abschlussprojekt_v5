import csv

def load_books():
    books = []
    try:
        with open("books.csv", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                books.append(Book(int(row[0]), row[1], row[2]))
    except FileNotFoundError:
        pass
    return books

def save_books(books):
    with open("books.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for book in books:
            writer.writerow([book.book_id, book.title, book.author])

def load_users():
    users = []
    try:
        with open("users.csv", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                users.append(User(int(row[0]), row[1]))
    except FileNotFoundError:
        pass
    return users

def save_users(users):
    with open("users.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for user in users:
            writer.writerow([user.user_id, user.name])