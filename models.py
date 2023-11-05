
from sqlalchemy import Date, create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_year = Column(Integer)

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    publication_year = Column(Integer) 
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship('Author')

    def __init__(self, title, publication_year, author_id):
        self.title = title
        self.publication_year = publication_year
        self.author_id = author_id

class Borrower(Base):
    __tablename__ = 'borrowers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    borrowing_date = Column(Date, nullable=False)
    return_date = Column(Date, nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'))

    book = relationship('Book')

    def __init__(self, name, borrowing_date, return_date, book_id):
        self.name = name
        self.borrowing_date = borrowing_date
        self.return_date = return_date
        self.book_id = book_id