from library import Library

def main():
    library = Library()
    library.load_data()
    
    while True:
        print("1. Buch hinzufügen")
        print("2. Benutzer hinzufügen")
        print("3. Buch ausleihen")
        print("4. Buch zurückgeben")
        print("5. Beenden")
        
        choice = input("Wähle eine Option: ")
        if choice == "1":
            title = input("Titel: ")
            author = input("Autor: ")
            library.add_book(title, author)
        elif choice == "2":
            name = input("Benutzername: ")
            library.add_user(name)
        elif choice == "3":
            user_id = input("Benutzer-ID: ")
            book_id = input("Buch-ID: ")
            library.loan_book(user_id, book_id)
        elif choice == "4":
            book_id = input("Buch-ID: ")
            library.return_book(book_id)
        elif choice == "5":
            break
    
    library.save_data()
    
if __name__ == "__main__":
    main()