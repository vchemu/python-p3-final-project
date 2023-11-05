from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Author, Book,Borrower

engine = create_engine('sqlite:///library.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_author(name, birth_year):
    author = Author(name=name, birth_year=birth_year)
    session.add(author)
    session.commit()

def get_authors():
    return session.query(Author).all()

def create_book(title, publication_year, author_id):
    book = Book(title=title, publication_year=publication_year, author_id=author_id)
    session.add(book)
    session.commit()

def get_books():
    return session.query(Book).all()

def create_borrower(name, borrowing_date, return_date, book_id):
    borrower = Borrower(name=name, borrowing_date=borrowing_date, return_date=return_date, book_id=book_id)
    session.add(borrower)
    session.commit()

def get_borrowers():
    return session.query(Borrower).all()