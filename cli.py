import sys
from database import create_author, get_authors, create_book, get_books, create_borrower, get_borrowers
from datetime import datetime, date

def main():
    authors = []
    books = []
    borrowers = []

    while True:
        print("\nLibrary Management System Menu:")
        print("1. Insert Author")
        print("2. List Authors with IDs")
        print("3. Add Book")
        print("4. List Books")
        print("5. Borrow a Book")
        print("6. List Borrowers")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter author's name: ")
            birth_year = int(input("Enter author's birth year: "))
            author = {'id': len(authors) + 1, 'name': name, 'birth_year': birth_year}
            authors.append(author)
            print("Author inserted successfully!")

        elif choice == '2':
            if authors:
                print("\nAuthors with IDs:")
                for author in authors:
                    print(f"ID: {author['id']}, Name: {author['name']} (Born {author['birth_year']})")
            else:
                print("No authors found in the database.")

        elif choice == '3':
            title = input("Enter the book title: ")
            publication_year = int(input("Enter the publication year: "))
            author_id = int(input("Enter the author's ID: "))
            book = {'id': len(books) + 1, 'title': title, 'publication_year': publication_year, 'author_id': author_id}
            books.append(book)
            print("Book added successfully!")

        elif choice == '4':
            if books:
                print("\nBooks:")
                for book in books:
                    author = next((author for author in authors if author['id'] == book['author_id']), None)
                    if author:
                        print(f"Title: {book['title']}, Author: {author['name']}, Year: {book['publication_year']}")
            else:
                print("No books found in the database.")

        elif choice == '5':
            book_id = int(input("Enter the book's ID to borrow: "))
            name = input("Enter your name: ")
            return_date_str = input("Enter the return date (YYYY-MM-DD): ")
            return_date = datetime.strptime(return_date_str, "%Y-%m-%d").date()
            borrowing_date = date.today()
            borrower = {'name': name, 'borrowing_date': borrowing_date, 'return_date': return_date, 'book_id': book_id}
            borrowers.append(borrower)

            print("Book borrowed successfully!")

        elif choice == '6':
            if borrowers:
                print("\nBorrowers:")
                for borrower in borrowers:
                    book = next((book for book in books if book['id'] == borrower['book_id']), None)
                    if book:
                        author = next((author for author in authors if author['id'] == book['author_id']), None)
                        if author:
                            print(f"Name: {borrower['name']}")
                            print(f"Borrowing Date: {borrower['borrowing_date']}")
                            print(f"Return Date: {borrower['return_date']}")
                            print(f"Book Title: {book['title']}, Author: {author['name']}\n")
            else:
                print("No borrowers found in the database.")

        elif choice == '7':
            print("Exiting the Library Management System.")
            sys.exit()

if __name__ == '__main__':
    main()
